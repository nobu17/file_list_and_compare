
from abc import ABCMeta, abstractmethod
import time


class PathBase(metaclass=ABCMeta):

    def __init__(self, path, name, created, updated):
        self.__path = path
        self.__name = name
        self.__created = created
        self.__updated = updated

    def __repr__(self):
        return f'[path:{self.path}, name:{self.name}, created:{self.created}, updated:{self.updated}]'

    @abstractmethod
    def to_csv_str(self) -> str:
        pass

    @property
    def path(self):
        return self.__path

    @property
    def name(self):
        return self.__name

    @property
    def created(self):
        return self.__created

    @property
    def updated(self):
        return self.__updated


class Directory(PathBase):

    def __init__(self, path, name, created, updated):
        super().__init__(path, name, created, updated)

    def __repr__(self):
        return f'[path:{self.path}, name:{self.name}, created:{self.created}, updated:{self.updated}]'

    def to_csv_str(self) -> str:
        return f'{self.path},{self.name},{self.created},{self.updated}'


class File(PathBase):

    def __init__(self, path, name, created, updated, dir, extension, size):
        super().__init__(path, name, created, updated)
        self.__size = size
        self.__dir = dir
        self.__extension = extension

    def __repr__(self):
        return f'[path:{self.path}, name:{self.name}, created:{self.created}, updated:{self.updated}, dir:{self.dir}, extension:{self.extension}, size:{self.size}]'

    def to_csv_str(self) -> str:
        return f'{self.path},{self.name},{self.created},{self.updated},{self.size},{self.extension},{self.dir}'

    @property
    def dir(self):
        return self.__dir

    @property
    def extension(self):
        return self.__extension

    @property
    def size(self):
        return self.__size
