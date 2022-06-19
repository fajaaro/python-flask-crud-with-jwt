import jwt
from datetime import datetime, timedelta
from flask import request
from app.main import app
from app.models.response import Response
from app.models.user import User
from app.repositories.user_repository import UserRepository
from passlib.hash import sha256_crypt

repo = UserRepository()

def generate_token(user: User):
    now = datetime.utcnow()
    access_token = jwt.encode({
        'user_id': user.id, 
        'exp': now + timedelta(minutes=30)
    }, app.config['SECRET_KEY'], "HS256")
    refresh_token = jwt.encode({
        'user_id': user.id, 
        'exp': now + timedelta(days=30)
    }, app.config['SECRET_KEY'], "HS256")
    
    return access_token, refresh_token

class AuthController:
    def register(self):
        res = Response(success=True)

        if not request.is_json:
            res.success = False
            res.error = "Accepted content-type: application/json"
            return res.to_json(), 400

        existing_user = repo.get_user_by_email(request.json.get("email"))
        if existing_user is not None:
            res.success = False
            res.error = 'Email is registered.'
            return res.to_json(), 400

        user = User(
            name = request.json.get("name"),
            email = request.json.get("email"),
            password = sha256_crypt.encrypt(request.json.get("password")),
        )
        user = repo.create(user)

        res.data = user.to_json()
        res.message = "New user has been registered."

        return res.to_json(), 201

    def login(self):
        res = Response(success=True)

        if not request.is_json:
            res.success = False
            res.error = "Accepted content-type: application/json"
            return res.to_json(), 400

        user = repo.get_user_by_email(request.json.get("email"))
        if user is None:
            res.success = False
            res.error = 'Email is not registered.'
            return res.to_json(), 400

        verified = sha256_crypt.verify(request.json.get("password"), user.password)

        if verified is True:
            user.last_login = datetime.now()
            user = repo.update(user)

            access_token, refresh_token = generate_token(user)

            res.data = {
                "user": user.to_json(),
                "token": {
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }
            }
            res.message = "Login success."
            return res.to_json()
        else:
            res.success = False
            res.error = "Wrong password."
            return res.to_json(), 400

    def refresh_token(self):
        res = Response(success=True)

        if not request.is_json:
            res.success = False
            res.error = "Accepted content-type: application/json"
            return res.to_json(), 400

        refresh_token = request.json.get("refresh_token")

        try:
            data = jwt.decode(refresh_token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except Exception as e:
            res.success = False
            res.error = "Refresh Token is invalid."
            return res.to_json(), 401

        user = repo.get_user_by_id(data['user_id'])
        if user is None:
            res.success = False
            res.error = "Refresh Token is invalid."
            return res.to_json(), 401
        
        access_token, _ = generate_token(user)

        res.data = {
            "access_token": access_token
        }
        res.message = "Access token has been updated."
        return res.to_json(), 200