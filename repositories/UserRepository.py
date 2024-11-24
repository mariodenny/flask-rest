from .BaseRepository import BaseRepository
from models.User import User

class UserRepository(BaseRepository):
    def find_by_email(self, email: str):
        return User.query.filter_by(email=email).first()

    def store(self, data: dict):
        return super().store(User, data)