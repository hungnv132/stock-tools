import pytz
from datetime import datetime
from flask import current_app
config = current_app.config

# from config import config


class DateTimeUtil(object):

    @staticmethod
    def now(tz_name=config['TIMEZONE']):
        return datetime.now(tz=pytz.timezone(tz_name))

    @staticmethod
    def date_to_string(date_obj, fmt="%d-%M-%Y %H:%M:%S"):
        """Convert a date object to a string
        """
        return datetime.strftime(date_obj, fmt)

    @staticmethod
    def string_to_date(date_string, fmt="%d-%M-%Y %H:%M:%S"):
        """Convert a string to a date object
        """
        return datetime.strptime(date_string, fmt)
