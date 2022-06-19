from flask import Blueprint
from controllers.auth_controller import AuthController

controller = AuthController()
api_auth = Blueprint('api_auth', __name__)

@api_auth.route('/register', methods = ['POST'])
def register():
    return controller.register()

@api_auth.route('/login', methods = ['POST'])
def login():
    return controller.login()

@api_auth.route('/refresh-token', methods = ['POST'])
def refresh_token():
    return controller.refresh_token()
