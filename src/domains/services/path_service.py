from domains.models.path_repository import AbstractPathRepository
from domains.models.compare import CompareResults, CompareInfo
from domains.models.path import PathBase, Directory, File
from typing import List


class PathService:

    def __init__(self, repository: AbstractPathRepository):
        self.__repository = repository

    def filter_list(self, path_list: List[PathBase], ignore_extensions: List[str], is_ignore_directory: bool) -> List[PathBase]:
        results = []
        for path in path_list:
            # check directory ignore option
            if(type(path) is Directory and is_ignore_directory):
                print("ignored dir:{}".format(path.path))
                continue
            # cehck ignore file exiteion
            if(type(path) is File):
                ext = path.extension
                if (ext.startswith('.')):
                    ext = ext[1:]
                if(ext in ignore_extensions):
                    print("ignored extension:{}".format(path.path))
                    continue
            results.append(path)

        return results

    def compre_from_env(self, path_list: List[PathBase]) -> CompareResults:
        success_count = 0
        fail_count = 0
        results = []

        for path in path_list:
            result = self._compre_from_env(path)
            results.append(result)
            if(result.isSucceed):
                success_count += 1
            else:
                fail_count += 1

        return CompareResults(results, success_count, fail_count)

    def _compre_from_env(self, compare_from: PathBase) -> CompareInfo:
        try:
            compare_to = self.__repository.find(compare_from.path)
            result = compare_from.compare(compare_to)
            # tuple0 is compare result, 1 is errormessage
            return CompareInfo(compare_from, result[0], result[1])
        except Exception as e:
            return CompareInfo(compare_from, False, "{}".format(e))
