from flask import jsonify

class ErrorHandler:

    @staticmethod
    def err_not_found(e):
        return jsonify({
            "code" : 404,
            "status" : "failed",
            "message" :e,
        }), 404
    
    @staticmethod
    def err_forbidden(e):
        return jsonify({
            "code" : 403,
            "status" : "failed",
            "message" :e,
        }), 403

    @staticmethod
    def err_unprocessable_content(e):
        return jsonify({
            "code" : 422,
            "status" : "failed",
            "message" :e,
        }), 422
    
    @staticmethod
    def err_internal_server_error(e):
        return jsonify({
            "code" : 500,
            "status" : "failed",
            "message" :e
        }), 500
    
    @staticmethod
    def err_unauthorized(e):
        return jsonify({
            "code" : 401,
            "status" : "failed",
            "message" :e,
        }), 401
    
    @staticmethod 
    def err_value_error(e):
        return jsonify({
            "code" : 400,
            "status" : "failed",
            "message" :e,
        }), 400