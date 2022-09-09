from endpoints_models.register.model import DataRegister, ResponseRegister


def test_true(app) -> None:
    """"""
    data = DataRegister.random()
    response = app.register.post(data=data, type_response=ResponseRegister)
    assert response.status_code == 201, "Check cod"
