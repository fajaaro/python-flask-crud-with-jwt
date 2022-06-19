from app.models.user import User
from app import db

from app.repositories.repository import Repository

class UserRepository(Repository):
    def get_all_user(self, order = "asc", limit = None) -> list:
        query = User.query.order_by(
            User.id.asc() if order == "asc"
            else User.id.desc()
        )

        users = None
        if limit is None:
            users = query.all()
        else:
            users = query.limit(limit)

        return users

    def get_user_by_id(self, id) -> User:
        return User.query.get(id)

    def get_user_by_email(self, email) -> User:
        return User.query.filter_by(email = email).first()
