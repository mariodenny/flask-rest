from flask import jsonify, request, Blueprint
from extensions import db

class Controller:
    def __init__(self, blueprint):
        self.blueprint = blueprint
        self.session = db.session  
