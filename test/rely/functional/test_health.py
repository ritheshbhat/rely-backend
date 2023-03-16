
def test_health_api(client):
    """Start with a blank database."""
    rv = client.get('/apis/health')
    print(f"data is ${rv.data}")
    assert b'"I\'m alive"' == rv.data.strip()
