
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config
db = SQLAlchemy()
mail = Mail()


def create_app(config_name):
    from app.stock import main as main_blue_print

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(main_blue_print)

    config[config_name].init_app(app)
    mail.init_app(app)
    db.init_app(app)

    # attach routes and custom error pages here
    return app