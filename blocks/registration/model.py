"""Response models."""


from pydantic import BaseModel


class RegistrationData(BaseModel):
    """Data to register new user."""

    username: str
    password: str


class SuccessfulRegistration(BaseModel):
    """Successful user registering response model."""

    message: str
    uuid: int
