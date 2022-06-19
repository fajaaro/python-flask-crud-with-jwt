from app.models.product import Product
from app import db
from app.repositories.repository import Repository

class ProductRepository(Repository):
    def get_all_product(self, order = "asc", limit = None) -> list:
        query = Product.query.order_by(
            Product.id.asc() if order == "asc"
            else Product.id.desc()
        )

        products = None
        if limit is None:
            products = query.all()
        else:
            products = query.limit(limit)

        return products

    def get_product_by_id(self, id) -> Product:
        return Product.query.get(id)

    def get_product_by_name(self, name) -> Product:
        return Product.query.filter_by(name = name).first()
        