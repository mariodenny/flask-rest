from extensions import db

class BaseService:
    def __init__(self):
        self.session = db.session