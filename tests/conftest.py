import pytest 

from ..model_api.app import create_app
from ..model_api.config import TestingConfig

@pytest.fixture
def app():
	app = create_app(config_object=TestingConfig)

	with app.app_context():
		yield app

@pytest.fixture
def flask_test_client(app):
	with app.test_client() as test_client:
		yield test_client
