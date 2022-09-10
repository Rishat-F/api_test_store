"""Sending requests."""


import requests
from requests import Response


class Client:
    """Client for sending requests."""

    def __init__(self, api_url):
        self.api_url = api_url

    @staticmethod
    def request(method: str, url: str, **kwargs) -> Response:
        """
        Send request.

        method:
            method for the new Request object:
                GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE
        url:
            URL for the new Request object
        **kwargs:
            params – (optional):
                Dictionary, list of tuples or bytes
                to send in the query string for the Request.
            data – (optional):
                Dictionary, list of tuples, bytes, or file-like object
                to send in the body of the Request.
            json – (optional):
                A JSON serializable Python object
                to send in the body of the Request.
            headers – (optional):
                Dictionary of HTTP Headers to send with the Request.
            auth – (optional):
                Auth tuple to enable Basic/Digest/Custom HTTP Auth.
            ...
        """
        return requests.request(method, url, **kwargs)
