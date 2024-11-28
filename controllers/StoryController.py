from flask import Blueprint, jsonify
from helper.JWTHelper import JWTHelper
from .Controller import Controller

story_blueprint = Blueprint('stories', __name__, url_prefix='/api/v1/stories')

class StoryController(Controller):
    def __init__(self):
        super().__init__()

    @story_blueprint.route('/test', methods=['GET'])
    @JWTHelper.jwt_required() 
    def test_jwt():
        current_name = JWTHelper.get_jwt_identity()
        return jsonify({
            "data": {"logged_in_as": current_name}
        })
