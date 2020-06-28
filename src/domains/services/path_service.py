from ..models.path_service import AbstractPathRepository

class PathService:

    def __init__(self, repository:AbstractPathRepository):
        self.__repository = repository

