"""Response models."""

from __future__ import annotations

from faker import Faker
from pydantic import BaseModel

fake = Faker()


class RegistrationData(BaseModel):
    """Data to register new user."""

    username: str
    password: str

    @staticmethod
    def random() -> RegistrationData:
        """Random username and password for registration."""
        return RegistrationData(username=fake.name(), password=fake.password())


class SuccessfulRegistration(BaseModel):
    """Successful user registering response model."""

    message: str
    uuid: int
