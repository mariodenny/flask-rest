from flask import Blueprint,jsonify,request
from .Controller import Controller

user_blueprint = Blueprint('user',__name__, url_prefix='/user')

class UserController(Controller):
    def __init__(self):
        super().__init__(user_blueprint)

    @staticmethod
    @user_blueprint.route('/ping', methods=['GET'])
    def ping():
        return jsonify({
            "message" : "Hello, Mom"
        })
