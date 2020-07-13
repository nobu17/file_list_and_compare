from .console_args import ConsoleArgs, Mode
from domains.applications.path_app_service import PathAppService, OutputFileListInput, CompareFileListInput


class ConsoleController:

    def __init__(self, service: PathAppService):
        self.__service = service

    def exec(self, args: ConsoleArgs):
        if (not args.isvalid):
            raise Exception(args.errormessage)

        if(args.mode == Mode.OUTPUT_LIST):
            print("output list mode")
            self.__service.output_file_list(OutputFileListInput(args.dir_path, args.ignore_extensions, args.is_ignore_directory))
            print("output file list csv is finished")
        elif (args.mode == Mode.COMPARE_FROM_FILE):
            print("compare mode")
            self.__service.compare_file(CompareFileListInput(args.compare_file_list_path))
