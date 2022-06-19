from datetime import datetime
from sqlalchemy import TIMESTAMP
from app import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(155), nullable = False)
    slug = db.Column(db.String(155), nullable = False, unique = True)
    price = db.Column(db.Float, nullable = False)
    created_at = db.Column(TIMESTAMP, default = datetime.now, onupdate = None)
    updated_at = db.Column(TIMESTAMP, onupdate = datetime.now)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'price': self.price,
            'created_at': str(self.created_at) if self.created_at is not None else self.created_at,
            'updated_at': str(self.updated_at) if self.updated_at is not None else self.updated_at
        }

    
