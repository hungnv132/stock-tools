from app import db
from app.stock.models import Company
from .base import DataAccessObject


class CompanyDAO(DataAccessObject):
    model = Company

    def find_by_id(self, object_id):
        pass
