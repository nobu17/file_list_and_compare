from abc import ABCMeta, abstractmethod
from typing import List
from .path import PathBase
from .compare import CompareResults
from .path_factory import AbstractPathFactory

class AbstractPathRepository(metaclass=ABCMeta):

    def __init__(self, factory: AbstractPathFactory):
        self.factory = factory

    @abstractmethod
    def findAll(self, path: str) -> List[PathBase]:
        pass

    @abstractmethod
    def find(self, path: str) -> PathBase:
        pass

    @abstractmethod
    def save(self, paths: List[PathBase]):
        pass

    @abstractmethod
    def save_compare_result(self, result: CompareResults):
        pass

    @abstractmethod
    def load(self, setting_path: str) -> List[PathBase]:
        pass
