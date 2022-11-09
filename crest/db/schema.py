from abc import abstractmethod, ABC


class Model:
    class Meta(ABC):
        def __init__(self):
            self.values = self.__dict__

        @property
        @abstractmethod
        def id(self):
            pass
