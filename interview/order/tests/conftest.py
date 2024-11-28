import pytest
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture(scope='session', autouse=True)
def setup_db(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        # Awful approach, I know :(
        import database
