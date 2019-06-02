from app import db
from app.stock.models import Industry
from .base import DataAccessObject


class IndustryDAO(DataAccessObject):
    model = Industry

    def find_by_id(self, object_id):
        pass
