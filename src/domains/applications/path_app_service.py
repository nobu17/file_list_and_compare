from typing import List
from domains.models.path_repository import AbstractPathRepository
# from domains.models.path_factory import AbstractPathFactory
from domains.services.path_service import PathService


class OutputFileListInput:

    def __init__(self, dir_path: str, ignore_extensions: List[str], is_ignore_directory: bool):
        self.__dir_path = dir_path
        self.__ignore_extensions = ignore_extensions
        self.__is_ignore_directory = is_ignore_directory

    @property
    def dir_path(self):
        return self.__dir_path

    @property
    def ignore_extensions(self):
        return self.__ignore_extensions       

    @property
    def is_ignore_directory(self):
        return self.__is_ignore_directory

    def validate(self):
        if(self.__dir_path is None):
            raise Exception("dir_path is empty")


class CompareFileListInput:

    def __init__(self, compare_file_path: str):
        self.__compare_file_path = compare_file_path

    @property
    def compare_file_path(self):
        return self.__compare_file_path

    def validate(self):
        if(self.__compare_file_path is None):
            raise Exception("compare_file_path is empty")


class PathAppService:

    def __init__(self, path_service: PathService, repository: AbstractPathRepository):
        self.__repository = repository
        self.__path_service = path_service

    def output_file_list(self, input: OutputFileListInput):
        if(input is None):
            raise Exception("input is null")

        input.validate()
        # load a file list
        file_list = self.__repository.findAll(input.dir_path)
        # filter
        file_list = self.__path_service.filter_list(file_list, input.ignore_extensions, input.is_ignore_directory)
        if(len(file_list) < 1):
            raise Exception("no file existed")

        # for file in file_list:
        #    print("file:{}".format(file))

        # save file list
        self.__repository.save(file_list)

    def compare_file(self, input: CompareFileListInput):
        if(input is None):
            raise Exception("input is null")

        input.validate()
        # load from csv file
        file_list = self.__repository.load(input.compare_file_path)
        if(len(file_list) < 1):
            raise Exception("no file listed from CSV")

        # compare each CSV file setting from actual enviroment
        result = self.__path_service.compre_from_env(file_list)
        # save a result as a file
        self.__repository.save_compare_result(result)



