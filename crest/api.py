from abc import abstractmethod
from typing import Literal


class Request:
    def __init__(self, request_line, headers, body):
        self.request_line = request_line
        self.headers = headers
        self.body = body


class Response:
    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body


class Handler:
    """
    API Handler classes are responsible for responding to API requests.
    """

    @property
    @abstractmethod
    def method(self) -> Literal['CONNECT', 'DELETE', 'HEAD', 'OPTIONS', 'POST', 'GET', 'PUT', 'TRACE']:
        pass

    @property
    @abstractmethod
    def route(self):
        pass

    @abstractmethod
    def handle(self, req: Request) -> Response:
        pass
