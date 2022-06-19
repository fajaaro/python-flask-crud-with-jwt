from datetime import datetime
from sqlalchemy import TIMESTAMP
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(155), nullable = False)
    email = db.Column(db.String(155), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    last_login = db.Column(TIMESTAMP)
    created_at = db.Column(TIMESTAMP, default = datetime.now, onupdate = None)
    updated_at = db.Column(TIMESTAMP, onupdate = datetime.now)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'last_login': str(self.last_login) if self.last_login is not None else self.last_login,
            'created_at': str(self.created_at) if self.created_at is not None else self.created_at,
            'updated_at': str(self.updated_at) if self.updated_at is not None else self.updated_at
        }
