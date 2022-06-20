from flask import request
from slugify import slugify
from app.helpers.main_helper import MainHelper
from app.models.product import Product
from app.models.response import Response
from app.repositories.product_repository import ProductRepository

repo = ProductRepository()

class ProductController:
    def index(self):
        order = request.args.get("order", default="desc")
        limit = request.args.get("limit", default=None)

        products = repo.get_all_product(order, limit)

        res = Response(
            success=True,
            data=MainHelper.serialize_objects(products),
            error=None,
            message="Success get products."
        )
        
        return res.to_json()

    def show(self, id):
        res = Response(success=True)

        product = repo.get_product_by_id(id)

        if product is None:
            res.success = False
            res.error = "Product not found."
            return res.to_json(), 404

        res.data = product.to_json()
        res.message = "Product with ID " + id + " has been found."

        return res.to_json()

    def store(self, user):
        res = Response(success=True)

        if not request.is_json:
            res.success = False
            res.error = "Accepted content-type: application/json"
            return res.to_json(), 400

        existing_product = repo.get_product_by_name(request.json.get("name"))
        if existing_product is not None:
            res.success = False
            res.error = 'Product with name "' + request.json.get("name") + '" is already exists.'
            return res.to_json(), 400

        product = Product(
            user_id = user.id,
            name = request.json.get("name"),
            slug = slugify(request.json.get("name")),
            price = request.json.get("price")
        )
        product = repo.create(product)

        res.data = product.to_json()
        res.message = "New product has been created."

        return res.to_json(), 201

    def update(self, id):
        res = Response(success=True)

        if not request.is_json:
            res.success = False
            res.error = "Accepted content-type: application/json"
            return res.to_json(), 400

        product = repo.get_product_by_id(id)

        if product is None:
            res.success = False
            res.error = "Product not found."
            return res.to_json(), 404

        existing_product = repo.get_product_by_name(request.json.get("name"))
        if existing_product is not None and existing_product is not product:
            res.success = False
            res.error = 'Product with name "' + request.json.get("name") + '" is already exists.'
            return res.to_json(), 400

        product.name = request.json.get("name")
        product.slug = slugify(request.json.get("name"))
        product.price = request.json.get("price")
        product = repo.update(product)

        res.data = product.to_json()
        res.message = "Product with ID " + id + " has been updated."

        return res.to_json()

    def delete(self, id):
        res = Response(success=True)

        product = repo.get_product_by_id(id)

        if product is None:
            res.success = False
            res.error = "Product not found."
            return res.to_json(), 404

        repo.delete(product)

        res.data = product.to_json()
        res.message = "Product " + product.name + " has been deleted."

        return res.to_json()
