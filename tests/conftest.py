"""Tests configurations."""


import pytest

from fixtures.application import Application

API_URL = "https://stores-tests-api.herokuapp.com"


@pytest.fixture(scope="session")
def app() -> Application:
    """Application fixture."""
    return Application(API_URL)
