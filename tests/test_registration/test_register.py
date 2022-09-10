"""API tests."""


from datetime import datetime

from blocks.registration.model import SuccessfulRegistration
from common.constants import Registration


def test_register_user(app):
    data = {"username": datetime.now().isoformat(), "password": "password"}
    response = app.registration.register_user(
        data=data, response_model=SuccessfulRegistration
    )
    assert response.status_code == 201
    assert response.data.message == Registration.SUCCESS
