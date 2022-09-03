from endpoints_models.register.api import Register
from utils.client import Client


class StoreApp:
    """App."""

    def __init__(self, url):
        self.url = url
        self.client = Client
        self.register = Register(self)
