from app import db
from app.stock.models import Exchange
from .base import DataAccessObject


class ExchangeDAO(DataAccessObject):
    model = Exchange

    def find_by_id(self, object_id):
        pass
