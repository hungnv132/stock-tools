# import os
# import pytest
# from app import create_app
#
# @pytest.fixture
# def app_context():
#     app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#     with app.app_context():
#         yield app
#
#
# @pytest.fixture
# def client(app):
#     return app.test_client()
#
#
# @pytest.fixture
# def runner(app):
#     return app.test_cli_runner()