import pytest

from endpoints_models.app import StoreApp


@pytest.fixture()
def app(request) -> StoreApp:
    url = request.config.getoption("--api-url")
    return StoreApp(url)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    )
