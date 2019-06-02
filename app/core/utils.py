import arrow
# from flask import current_app
#
# config = current_app.config


def date_to_str(date_object, fmt="DD-MM-YYYY HH:mm:ss"):
    pass


def str_to_date(date_string, fmt="DD-MM-YYYY"):
    arrow.get(date_string, fmt)