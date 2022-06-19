from flask import Blueprint

from app.models.response import Response

api_index = Blueprint('api_index', __name__)

@api_index.route('/')
def index():
    res = Response(True, None, None, "Welcome to Fajar Flask Rest API!")

    return res.to_json()
