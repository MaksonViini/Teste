import pytest
import requests

def test_data():
    data = {
    'id': 1,
    'value': 10
    }

    response = requests.get('http://localhost:5000/model')
    assert response.status_code == 200
    assert response.json() == data

def test_create():
    data = {
    'id': 1,
    'value': 10
    }

    response = requests.post('http://localhost:5000/model', json=data)
    assert response.status_code == 200
    assert response.json() == data