import requests
from abc import ABCMeta, abstractmethod
from datetime import datetime

from app.core.utils import date_to_str


ALLOWED_METHOD = ['GET', 'POST']
DEFAULT_HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}


class AbstractFetcher(metaclass=ABCMeta):

    def __init__(self, url='', params={}):
        self.url = url
        self.params = params

    def prepare_url(self):
        return self.url

    @classmethod
    def prepare_headers(cls):
        return DEFAULT_HEADERS

    def prepare_request(self, **kwargs):
        kwargs['headers'] = self.prepare_headers()
        kwargs['url'] = self.prepare_url()
        return kwargs

    def request_get(self, **kwargs):
        kwargs = self.prepare_request(**kwargs)
        return requests.get(**kwargs)

    def request_post(self, **kwargs):
        kwargs = self.prepare_request(**kwargs)
        return requests.post(**kwargs)

    @abstractmethod
    def fetch(self):
        raise NotImplemented("You must implement the function "
                             "'fetch()'")


class StockFetcherInterface(metaclass=ABCMeta):

    @abstractmethod
    def fetch_companies_list(self):
        raise NotImplemented("You must implement the function "
                             "'fetch_companies_list()'")

    @abstractmethod
    def fetch_exchange_data(self, company, from_date, to_date):
        raise NotImplemented("You must implement the function "
                             "'fetch_companies_list()'")

    @abstractmethod
    def fetch_foreign_exchange_data(self, company, from_date, to_date):
        raise NotImplemented("You must implement the function "
                             "'fetch_foreign_exchange_data()'")

#
# class AbstractStockPuller(metaclass=ABCMeta):
#     url = None
#     method = 'GET'
#     default_headers = {
#         'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
#     }
#     default_payload = {}
#
#     def __init__(self, symbol, start_date, end_date, **kwargs):
#         self._symbol = symbol
#         self._start_date = start_date
#         self._end_date = end_date
#         self.__dict__.update(**kwargs)
#         self._validate()
#
#     def _validate(self):
#         if not self.url:
#             return ValueError("Please provide 'url' for this puller.")
#         if not self.method:
#             return ValueError("Please provide 'method' for this puller.")
#         if not self._symbol:
#             return ValueError("Please provide 'symbol' for this puller.")
#
#     def get_url(self):
#         return self.url
#
#     def get_method(self):
#         method = self.method
#         if method not in ALLOWED_METHOD:
#             raise ValueError("The system does not support "
#                              "the method: '%s'" % self.method)
#         return method.lower()
#
#     def get_headers(self, **kwargs):
#         """
#         To crawl data successfully, need some special header parameters
#         """
#         return self.default_headers
#
#     def get_payload(self):
#         """
#         Attach some body data to the request
#         """
#         return self.default_payload
#
#     def get_cookies(self):
#         return {}
#
#     @property
#     def symbol(self):
#         return self._symbol.lower()
#
#     @property
#     def start_date(self):
#         if isinstance(self._start_date, str):
#             return self._start_date
#         if isinstance(self._start_date, datetime):
#             return date_to_str(self._start_date)
#
#     @start_date.setter
#     def start_date(self, start_date):
#         self._start_date = start_date
#
#     @property
#     def end_date(self):
#         if isinstance(self._end_date, str):
#             return self._end_date
#         if isinstance(self._end_date, datetime):
#             return date_to_str(self._end_date)
#
#     @end_date.setter
#     def end_date(self, end_date):
#         self._end_date = end_date
#
#     @abstractmethod
#     def clean_data(self, response):
#         """
#         After crawling data from the url, need to clean and convert the data
#         to right data type in python.
#         """
#         pass
#
#     def get(self, **kwargs):
#         return requests.get(**kwargs)
#
#     def post(self, **kwargs):
#         return requests.post(**kwargs)
#
#     def send_request(self, url=None, **kwargs):
#         method = self.get_method()
#         kwargs['headers'] = self.get_headers()
#         kwargs['url'] = url or self.get_url()
#
#         try:
#             response = getattr(self, method)(**kwargs)
#         except Exception as ex:
#             print(ex)
#             response = []
#         return response
#
#     def _pull_data(self, **kwargs):
#         kwargs['cookies'] = self.get_cookies()
#         kwargs['data'] = self.get_payload()
#
#         response = self.send_request(**kwargs)
#         if response:
#             cleaned_results = self.clean_data(response.json())
#             return cleaned_results
#         else:
#             return []
#
#
# class TradingDataPuller(AbstractStockPuller):
#
#     def pull_trading_data(self, **kwargs):
#         """
#         Pull data from outside source
#         :param kwargs: some options for processing
#         :return: List of dictionary
#         """
#         return self._pull_data(**kwargs)
#
#
# class ForeignTradingDataPuller(AbstractStockPuller):
#     """
#     # An abstract class for crawling foreign exchange data
#     """
#     def pull_foreign_trading_data(self, **kwargs):
#         """
#         Pull data from outside source
#         :param kwargs: some options for processing
#         :return: List of dictionary contains foreign_buy_volume,
#                   foreign_buy_value, foreign_sell_volume
#                   foreign_sell_value, traded_at
#         """
#         return self._pull_data(**kwargs)
