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
            }), 201
        except ValueError as e:
            return ErrorHandler.err_value_error(str(e))
        except Exception as e:
            return ErrorHandler.err_internal_server_error(str(e))
        
    @staticmethod
    @user_blueprint.route('/login', methods=['POST'])
    def login():
        try:    
            request_data = request.get_json()
            if not request_data:
                return ErrorHandler.err_required_val()
            
            user = UserService().login(request_data)

            return jsonify({
                "code" : 200,
                "message" : "request success",
                "data" : user
            })
        
        except ValueError as e:
            return ErrorHandler.err_value_error(str(e))
        except ValueError as e:
            return ErrorHandler.err_internal_server_error(str(e))
