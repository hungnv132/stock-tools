import click
from flask.cli import AppGroup
from app.stock.fetcher import VNDirectFetcher
from app.stock.dao import IndustryDAO, ExchangeDAO, CompanyDAO

stock_cli = AppGroup('stock')

industry_dao = IndustryDAO()
exchange_dao = ExchangeDAO()
company_dao = CompanyDAO()


@stock_cli.command('fetch-companies')
def fetch_companies_list():
    stock_fetcher = VNDirectFetcher()
    companies_list = stock_fetcher.fetch_companies_list()

    for data in companies_list:
        if not data['industryName'] or not data['floor']:
            continue

        industry, created = industry_dao.get_or_create(name=data['industryName'])
        exchange, created = exchange_dao.get_or_create(name=data['floor'])
        company, created = company_dao.get_or_create(
            symbol=data['symbol'],
            default={
                'name': data['companyName'],
                'industry': industry,
                'exchange': exchange,
            }
        )
        if created:
            print(f"Created company: '{company.name}'")
