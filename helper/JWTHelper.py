from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

class JWTHelper:
    @staticmethod
    def generate_access_token(name: str):
        return create_access_token(identity=name)

    @staticmethod
    def jwt_required():
        return jwt_required()

    @staticmethod
    def get_jwt_identity():
        return get_jwt_identity()
