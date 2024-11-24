from controllers.UserController import user_blueprint

def register_routes(app):
    app.register_blueprint(user_blueprint)