from flask_bcrypt import Bcrypt
from datetime import datetime
from .BaseService import BaseService
from repositories.UserRepository import UserRepository
from helper.JWTHelper import JWTHelper

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
    
    def login(self,request_data:dict):
        required_fields = ['email', 'password']
        for field in required_fields:
            if field not in request_data:
                raise ValueError(f"Missing required field: {field}")
            
        user = self.user_repository.find_by_email(request_data['email'])
        if user.email != request_data['email']:
            raise ValueError("email or password missmatch")    
        
        access_token = JWTHelper.generate_access_token(user.id)

        return {
            "name" : user.name,
            "email" : user.email,
            "access_token" : access_token,
        }

         