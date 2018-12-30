import pytest
from myapp import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'localhost.localdomain'
    client = app.test_client()

    return client