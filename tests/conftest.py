import pytest
from myapp import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    return client