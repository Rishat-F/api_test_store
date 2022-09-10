"""Application fixture."""


from blocks.registration.api import Registration
from utils.request import Client


class Application:
    """Application for testing."""

    def __init__(self, api_url):
        self.client = Client(api_url)
        self.registration = Registration(self.client)
