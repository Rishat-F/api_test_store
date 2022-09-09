"""API тесты."""


from datetime import datetime

import requests


def test_register_user() -> None:
    """Регистрация нового пользователя."""
    API_URL = "https://stores-tests-api.herokuapp.com"
    ENDPOINT = "/register"
    data = {"username": datetime.now().isoformat(), "password": "password"}
    response = requests.post(API_URL + ENDPOINT, data=data)
    assert response.status_code == 201
    assert isinstance(response.json().get("message"), str)
    assert isinstance(response.json().get("uuid"), int)
