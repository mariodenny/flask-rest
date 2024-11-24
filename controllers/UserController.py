from flask import Blueprint, jsonify, request
from .Controller import Controller
from services.UserService import UserService
from error_handlers import ErrorHandler

user_blueprint = Blueprint('user', __name__, url_prefix='/api/v1/users')

class UserController(Controller):
    def __init__(self):
        super().__init__()
        self.user_service = UserService()

    @staticmethod
    @user_blueprint.route('/register', methods=['POST'])
    def register():
        try:
            request_data = request.get_json()
            if not request_data:
                return jsonify({'error': 'No data provided'}), 400
                
            user = UserService().register(request_data)
            return jsonify({
                'status': 'success',
                'message': 'User registered successfully',
                'data': user.to_dict()  
            }), 201
        except ValueError as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 400
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500