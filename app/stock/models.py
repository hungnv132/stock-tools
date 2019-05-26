# from sqlite3 import dbapi2 as sqlite
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine('sqlite+pysqlite:///sqlite3.db', module=sqlite, echo=True)
#
# Session = sessionmaker()
# Session.configure(bind=engine)
#
# Base = declarative_base()
#
#
# class User(Base):
#     __tablename__ = 'tbl_users'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     address = Column(String)
#
#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', nickname='%s')>" % (
#             self.name, self.fullname, self.nickname
#         )
#
#
# class Exchange:
#     __tablename__ = 'stock_exchange'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, unique=True, nullable=False)
#     description = Column(String)
#
#
# class Industry:
#     __tablename__ = 'stock_industry'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, unique=True, nullable=False)
#     description = Column(String)
#
#
# class Company:
#     __tablename__ = 'stock_company'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     symbol = Column(String, unique=True, nullable=False)
#     description = Column(String)
#
#
# if __name__ == '__main__':
#     # Base.metadata.create_all(engine)
#     ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
#     session = Session()
#     session.add(ed_user)
#     session.commit()
