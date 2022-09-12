"""Response models."""


from faker import Faker
from pydantic import BaseModel

fake = Faker()


class RegistrationData(BaseModel):
    """Data to register new user."""

    username: str
    password: str

    @staticmethod
    def random():  # type: ignore
        """Random username and password for registration."""
        return RegistrationData(username=fake.username(), password=fake.password())


class SuccessfulRegistration(BaseModel):
    """Successful user registering response model."""

    message: str
    uuid: int
