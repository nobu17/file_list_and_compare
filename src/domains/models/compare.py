from .path import PathBase
from typing import List

class CompareInfo:
    def __init__(self, info: PathBase, isSucceed: bool, error_message: str):
        self.__info = info
        self.__isSucceed = isSucceed
        self.__error_message = error_message

    def to_csv_str(self) -> str:
        return self.info.to_csv_str() + f',{self.isSucceed},{self.error_message}' 

    @property
    def info(self) -> PathBase:
        return self.__info

    @property
    def isSucceed(self) -> bool:
        return self.__isSucceed

    @property
    def error_message(self) -> str:
        return self.__error_message


class CompareResults:
    def __init__(self, results: List[CompareInfo], success_count: int, fail_count: int):
        self.__results = results
        self.__success_count = success_count
        self.__fail_count = fail_count

    @property
    def results(self) -> List[CompareInfo]:
        return self.__results

    @property
    def success_count(self) -> int:
        return self.__success_count

    @property
    def fail_count(self) -> int:
        return self.__fail_count
