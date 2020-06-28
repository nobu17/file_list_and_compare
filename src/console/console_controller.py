from .console_args import ConsoleArgs
from domains.applications.path_app_service import PathAppService, OutputFileListInput

class ConsoleController:

    def __init__(self, service:PathAppService):
        self.__service = service

    def exec(self, args: ConsoleArgs):
        if (not args.isvalid):
            raise Exception(args.errormessage)

        file_list = self.__service.output_file_list(OutputFileListInput(args.dir_path))


