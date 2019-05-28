from app import db
from app.core.models import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Exchange(BaseModel):
    __tablename__ = 'stock_exchange'
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    companies = relationship('Company', backref='exchange')


class Industry(BaseModel):
    __tablename__ = 'stock_industry'
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    companies = relationship('Company', backref='industry')


class Company(BaseModel):
    __tablename__ = 'stock_company'
    name = Column(String, nullable=False)
    symbol = Column(String, unique=True, nullable=False)
    description = Column(String)
    exchange_id = Column(Integer, ForeignKey('stock_exchange.id'),
                         nullable=False)
    industry_id = Column(Integer, ForeignKey('stock_industry.id'),
                         nullable=False)