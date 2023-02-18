from app import app
from chalice.test import Client


def test_index():
    with Client(app) as client:
        response = client.http.get("/")
        assert response.json_body == {"hello": "world"}
