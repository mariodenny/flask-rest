from flask import jsonify

class ErrorHandler:

    @staticmethod
    def err_not_found(e):
        return jsonify({
            "error" : "resource not found"
        }), 404
    
    @staticmethod
    def err_forbidden(e):
        return jsonify({
            "error" : "forbidden"
        }), 403

    @staticmethod
    def err_unprocessable_content(e):
        return jsonify({
            "error" : "unprocessable content"
        }), 422
    
    @staticmethod
    def err_internal_server_error(e):
        return jsonify({
            "error" : "internal server error"
        }), 500
    
    @staticmethod
    def err_unauthorized(e):
        return jsonify({
            "error" : "Unauthorized"
        }), 401
    