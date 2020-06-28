from domains.models.path_service import AbstractPathRepository
# from domains.models.path_factory import AbstractPathFactory
from domains.services.path_service import PathService


class OutputFileListInput:

    def __init__(self, dir_path: str):
        self.__dir_path = dir_path

    @property
    def dir_path(self):
        return self.__dir_path

    def validate(self):
        if(self.__dir_path is None):
            raise Exception("dir_path is empty")


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
        if(len(file_list) < 1):
            raise Exception("no file existed")

        for file in file_list:
            print("file:{}".format(file))

        # save file list
        self.__repository.save(file_list)
