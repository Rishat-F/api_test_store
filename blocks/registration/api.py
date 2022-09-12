"""Operations in registration block of API."""


from typing import Optional, Tuple

from pydantic import BaseModel
from requests import Response

from blocks.registration.model import RegistrationData
from utils.logger import log
from utils.request_sender import Client
from utils.validator import Validator


class Registration(Validator):
    """Registration block."""

    def __init__(self, client: Client):
        self.client = client

    REGISTER_USER = "/register"

    @log("POST /register")  # type: ignore
    def register_user(
        self, data: RegistrationData, response_model: Optional[BaseModel] = None
    ) -> Tuple[Response, Optional[Exception]]:
        """Register new user."""
        response = self.client.request(
            "POST", self.client.api_url + self.REGISTER_USER, json=data
        )
        return self.transform(response, response_model=response_model)
