
from app import db
from app.core.utils import DateTimeUtil
from sqlalchemy import Column, Integer, DateTime


class BaseModel(db.Model):

    __abstract__ = True

    id = Column(Integer, primary_key=True)
    date_created = Column(DateTime,
                          default=DateTimeUtil.now)
    date_modified = Column(DateTime,
                           default=DateTimeUtil.now,
                           onupdate=DateTimeUtil.now)
