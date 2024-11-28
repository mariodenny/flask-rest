from extensions import db
from typing import Dict, Any

class BaseRepository:
    def __init__(self):
        self.session = db.session

    def store(self, model_class, data: Dict[str, Any]):
        try:
            instance = model_class(**data)
            self.session.add(instance)
            self.session.commit()
            return instance
        except Exception as e:
            self.session.rollback()
            raise e

    def update(self, model_class, id: int, data: Dict[str, Any]):
        try:
            instance = model_class.query.get(id)
            if instance:
                for key, value in data.items():
                    setattr(instance, key, value)
                self.session.commit()
                return instance
            return None
        except Exception as e:
            self.session.rollback()
            raise e

    def delete(self, model_class, id: int):
        try:
            instance = model_class.query.get(id)
            if instance:
                self.session.delete(instance)
                self.session.commit()
                return True
            return False
        except Exception as e:
            self.session.rollback()
            raise e
        
    def firstrow(self, model_class, id:int):
        try:
            instance = model_class.query.get(id)
            if instance:
                self.session.query(instance).one()
                self.session.commit()
                return True
            return False
        except Exception as e:
            raise e