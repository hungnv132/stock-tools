import json
from .base import AbstractFetcher, StockFetcherInterface

COMPANIES_LIST_URL = "https://finfo-api.vndirect.com.vn/stocks?status=all"
EXCHANGE_DATA_URL = ''
FOREIGN_EXCHANGE_DATA_URL = ''
CONTENT_TYPE = 'application/json'


class CompanyListFetcher(AbstractFetcher):
    """
    Pull list of companies from VNDirect server.
    """

    def fetch(self):
        response = self.request_get()
        content_type_response = response.headers['Content-Type']
        companies = []
        if CONTENT_TYPE in content_type_response:
            content = json.loads(response.content)
            companies = content['data']
        return companies


class ExchangeDataFetcher(AbstractFetcher):

    def fetch(self):
        pass


class ForeignExchangeDataFetcher(AbstractFetcher):

    def fetch(self):
        pass


class VNDirectFetcher(StockFetcherInterface):

    def fetch_companies_list(self):
        fetcher = CompanyListFetcher(url=COMPANIES_LIST_URL)
        return fetcher.fetch()

    def fetch_exchange_data(self, company, from_date, to_date):
        pass

    def fetch_foreign_exchange_data(self, company, from_date, to_date):
        pass
