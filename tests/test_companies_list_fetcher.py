from app.stock.fetcher.vndirect import (
    COMPANIES_LIST_URL, CompanyListFetcher
)


def test_vnd_companies_fetcher():
    fetcher = CompanyListFetcher(url=COMPANIES_LIST_URL)
    companies_list = fetcher.fetch()
    assert len(companies_list) > 1500
    import pdb; pdb.set_trace()