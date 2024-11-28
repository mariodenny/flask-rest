from controllers.UserController import user_blueprint
from controllers.StoryController import story_blueprint

def register_routes(app):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(story_blueprint)