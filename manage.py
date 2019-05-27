import os
from app import create_app
from flask_script import Manager
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

from app.auth.models import User


@manager.command
def hello():
    users = User.query.all()
    print(users)


if __name__ == '__main__':
    manager.run()
