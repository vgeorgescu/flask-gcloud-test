from flask import url_for
from myapp import app

def test_home(client):
    """Check the home page"""
    response = client.get('/')
    assert b'La multi ani!' in response.data


def test_dashboard_redirect(client):
    """Check that dashboard redirects to login when unauthenticated"""
    with app.app_context():
        response = client.get('/dashboard')
        assert response.status_code == 302
        assert response.location == url_for('auth.login', _external=True)
