from flask_bcrypt import Bcrypt
from datetime import datetime
from .BaseService import BaseService
from repositories.UserRepository import UserRepository

class UserService(BaseService):
    def __init__(self):
        super().__init__()
        self.user_repository = UserRepository()
        self.bcrypt = Bcrypt()

    def register(self, data: dict):
        required_fields = ['name', 'email', 'password']
        for field in required_fields:
            if field not in data:
                raise ValueError(f'Missing required field: {field}')

        if self.user_repository.find_by_email(data['email']):
            raise ValueError('Email already registered')

        user_data = {
            'name': data['name'],
            'email': data['email'],
            'password': self.bcrypt.generate_password_hash(data['password']).decode('utf-8'),
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }

        return self.user_repository.store(user_data)