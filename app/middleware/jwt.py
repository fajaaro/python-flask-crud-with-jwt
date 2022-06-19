from functools import wraps

import jwt
from app.models.response import Response
from flask import request
from app.main import app
from app.repositories.user_repository import UserRepository

user_repository = UserRepository()

def json_web_token(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        res = Response(success=True)
       
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]

        if token is None:
            res.success = False
            res.error = "A valid token is missing."
            return res.to_json(), 400

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except Exception as e:
            res.success = False
            res.error = "Token is invalid."
            return res.to_json(), 401

        user = user_repository.get_user_by_id(data['user_id'])
        if user is None:
            res.success = False
            res.error = "Token is invalid."
            return res.to_json(), 401

        return f(user, *args, **kwargs)
    return decorator