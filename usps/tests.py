""" USPS API unit tests """
import json
from http import HTTPStatus
from .main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    # response = client.get("/")
    # assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}
    pass