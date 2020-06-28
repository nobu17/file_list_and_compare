
from abc import ABCMeta, abstractmethod
from .path import PathBase

class AbstractPathFactory(metaclass=ABCMeta):

    @abstractmethod
    def create(self, path: str) -> PathBase:
        pass
