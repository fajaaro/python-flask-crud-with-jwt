from flask import Blueprint
from app.middleware.jwt import json_web_token
from controllers.product_controller import ProductController

controller = ProductController()
api_products = Blueprint('api_products', __name__)

@api_products.route('/')
@json_web_token
def index(user):
    return controller.index()

@api_products.route('/<id>')
@json_web_token
def show(user, id):
    return controller.show(id)

@api_products.route('/', methods = ['POST'])
@json_web_token
def store(user):
    return controller.store()

@api_products.route('/<id>', methods = ['PUT'])
@json_web_token
def update(user, id):
    return controller.update(id)

@api_products.route('/<id>', methods = ['DELETE'])
@json_web_token
def delete(user, id):
    return controller.delete(id)
