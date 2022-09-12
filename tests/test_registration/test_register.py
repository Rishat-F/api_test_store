"""API tests."""


from blocks.registration.model import RegistrationData, SuccessfulRegistration
from common.constants import Registration


def test_register_user(app):
    data = RegistrationData.random().dict()
    response = app.registration.register_user(
        data=data, response_model=SuccessfulRegistration
    )
    assert response.status_code == 201
    assert response.data.message == Registration.SUCCESS
