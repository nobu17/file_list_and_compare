
from abc import ABCMeta, abstractmethod
import time
from datetime import datetime
from typing import Tuple


class PathBase(metaclass=ABCMeta):

    def __init__(self, path: str, name: str, created: datetime, updated: datetime):
        self.__path = path
        self.__name = name
        self.__created = created
        self.__updated = updated

    def __repr__(self):
        return f'[path:{self.path}, name:{self.name}, created:{self.created_str}, updated:{self.updated_str}]'

    @staticmethod
    def _datetime_to_str(dt: datetime) -> str:
        return dt.strftime("%Y/%m/%d %H:%M")

    @abstractmethod
    def to_csv_str(self) -> str:
        pass

    @abstractmethod
    def compare(self, target) -> Tuple[bool, str]:
        if(target is None):
            return (False, "compare target is null")
        if(self.path != target.path):
            return (False, "path is different")
        if(self.name != target.name):
            return (False, "name is different")
        if(self.created_str != target.created_str):
            return (False, "created is different")
        if(self.updated_str != target.updated_str):
            return (False, "updated is different")

        return (True, "")

    @property
    def path(self) -> str:
        return self.__path

    @property
    def name(self) -> str:
        return self.__name

    @property
    def created(self) -> datetime:
        return self.__created

    @property
    def updated(self) -> datetime:
        return self.__updated

    @property
    def created_str(self) -> str:
        return PathBase._datetime_to_str(self.__created)

    @property
    def updated_str(self) -> str:
        return PathBase._datetime_to_str(self.__updated)


class Directory(PathBase):

    def __init__(self, path: str, name: str, created: datetime, updated: datetime):
        super().__init__(path, name, created, updated)

    def __repr__(self):
        return f'[path:{self.path}, name:{self.name}, created:{self.created_str}, updated:{self.updated_str}]'

    def to_csv_str(self) -> str:
        return f'{self.path},{self.name},{self.created_str},{self.updated_str}'

    def compare(self, target) -> Tuple[bool, str]:
        return super().compare(target)


class File(PathBase):

    def __init__(self, path: str, name: str, created: datetime, updated: datetime, dir: str, extension: str, size: int):
        super().__init__(path, name, created, updated)
        self.__size = size
        self.__dir = dir
        self.__extension = extension

    def __repr__(self):
        return f'[path:{self.path}, name:{self.name}, created:{self.created_str}, updated:{self.updated_str}, dir:{self.dir}, extension:{self.extension}, size:{self.size}]'

    def to_csv_str(self) -> str:
        return f'{self.path},{self.name},{self.created_str},{self.updated_str},{self.dir},{self.extension},{self.size}'

    def compare(self, target) -> Tuple[bool, str]:
        result = super().compare(target)
        if(not result[0]):
            return result

        if (self.dir != target.dir):
            return (False, "dir is different.from:{0}, to:{1}".format(self.dir, target.dir))
        if (self.extension != target.extension):
            return (False, "extension is different")
        if (self.size != target.size):
            return (False, "size is different")
        
        return (True, "")

    @property
    def dir(self) -> str:
        return self.__dir

    @property
    def extension(self) -> str:
        return self.__extension

    @property
    def size(self) -> int:
        return self.__size
