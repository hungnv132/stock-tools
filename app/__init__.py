import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from sqlalchemy import MetaData
from config import config

flask_app_names = [
    'auth',
    'stock'
]
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
mail = Mail()


def create_app(config_name='default'):
    config_name = os.getenv('FLASK_CONFIG') or config_name

    from app.stock import main as main_blue_print
    # Must import models here for Flask-Migrate detect changes.

    app = Flask(__name__)

    # push application context manually
    with app.app_context():
        app.config.from_object(config[config_name])
        app.register_blueprint(main_blue_print)

        register_models()
        register_command_lines(app)

        config[config_name].init_app(app)

        migrate = Migrate(app, db)
        # Init apps
        mail.init_app(app)
        db.init_app(app)
        migrate.init_app(app)

    # attach routes and custom error pages here
    return app


def register_models():
    from app.auth.models import User
    from app.stock.models import Exchange, Industry, Company


def register_command_lines(flask_app):
    from app.stock.commands import stock_cli

    command_functions = [stock_cli]

    for function in command_functions:
        flask_app.cli.add_command(function)
