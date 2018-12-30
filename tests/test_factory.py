def test_home(client):
    """Check the home page"""
    response = client.get('/')
    assert b'Hello, world!' in response.data