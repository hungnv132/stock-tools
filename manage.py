import os
from app import create_app, db
from flask_script import Manager
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


from app.auth.models import User
from app.stock.models import Exchange, Industry, Company


@manager.command
def hello():
    users = User.query.all()
    print(users)


@manager.command
def init_data():
    exchange = Exchange(name='HSX')
    industry = Industry(name='Tech')
    db.session.add(exchange)
    db.session.add(industry)
    db.session.commit()


@manager.command
def init_data():
    exchange_hsx = Exchange.query.filter_by(name='HSX').first()
    industry_tech = Industry.query.filter_by(name='Tech').first()
    company = Company(name='Big company', symbol='ABC', exchange=exchange_hsx,
                      industry=industry_tech)
    # import pdb; pdb.set_trace()
    db.session.add(company)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
