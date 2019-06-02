from app import db
from abc import ABCMeta, abstractmethod


class DataAccessObject(metaclass=ABCMeta):
    model = None

    @abstractmethod
    def find_by_id(self, object_id):
        raise NotImplemented("You must implement the function"
                             "'find_by_id()")

    def get_or_create(self,  default={}, **params,):
        if not self.model:
            raise ValueError("The 'model' property must be not None ")
        created = False
        instance = db.session.query(self.model).filter_by(**params).first()
        if not instance:
            params.update(default)
            instance = self.model(**params)
            db.session.add(instance)
            db.session.commit()
            created = True
        return instance, created
