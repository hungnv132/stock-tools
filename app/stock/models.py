from app.core.models import BaseModel
from sqlalchemy import Column, Integer, String


class Exchange(BaseModel):
    __tablename__ = 'stock_exchange'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)


class Industry(BaseModel):
    __tablename__ = 'stock_industry'
    name = Column(String, unique=True, nullable=False)
    description = Column(String)


class Company:
    __tablename__ = 'stock_company'
    name = Column(String, nullable=False)
    symbol = Column(String, unique=True, nullable=False)
    description = Column(String)

