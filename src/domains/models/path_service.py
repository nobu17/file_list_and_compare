from abc import ABCMeta, abstractmethod
from typing import List
from .path import PathBase
from .path_factory import AbstractPathFactory


class AbstractPathRepository(metaclass=ABCMeta):

    def __init__(self, factory: AbstractPathFactory):
        self.factory = factory

    @abstractmethod
    def findAll(self, path: str) -> List[PathBase]:
        pass

    @abstractmethod
    def save(self, paths: List[PathBase]):
        pass

    @abstractmethod
    def load(self, setting_path: str) -> List[PathBase]:
        pass
