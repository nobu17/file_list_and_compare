
from abc import ABCMeta, abstractmethod
from .path import PathBase


class AbstractPathFactory(metaclass=ABCMeta):

    @abstractmethod
    def create(self, path: str) -> PathBase:
        pass

    @abstractmethod
    def create_from_csv_str(self, csv_str: str) -> PathBase:
        pass
