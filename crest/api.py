from abc import abstractmethod
from typing import Literal


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
    def handle(self, req) -> map:
        pass
