import argparse
from enum import Enum
from pathlib import Path


class Mode(Enum):
    OUTPUT_LIST = 1
    COMPARE_FROM_FILE = 2


class ConsoleArgs:

    def __init__(self):
        self._init_variable()
        self._check_param()

    def _init_variable(self):
        self.isvalid = True
        self.errormessage = ""
        self.dir_path = ""
        self.compare_file_list_path = ""
        self.mode = Mode.OUTPUT_LIST

        parser = argparse.ArgumentParser(
            description='this is a tool for outputting and comparing file list', add_help=True)
        parser.add_argument('path', help="target-directory or filie-list")
        parser.add_argument('-e', '--ignore_extensions',
                            help='ignoring extensions for outputing list.(ex:txt,log.jpg)', default='')
        parser.add_argument('-d', '--ignore_directory',
                            help='ignoring directory for outputing listt.', action='store_true')
        args = parser.parse_args()

        self.__temp_dir = args.path
        self.ignore_extensions = args.ignore_extensions.split(',')
        self.is_ignore_directory = args.ignore_directory

    def _check_param(self):
        
        if(not self.__temp_dir):
            self.isvalid = False
            self.errormessage = "directory or csv path is needed."
            return

        # check mode
        p = Path(self.__temp_dir)
        if (p.is_file() and ''.join(p.suffixes).lower() == ".csv"):
            self.mode = Mode.COMPARE_FROM_FILE
            self.compare_file_list_path = self.__temp_dir
            return

        if (not p.is_dir()):
            self.isvalid = False
            self.errormessage = "指定されたファイルはフォルダではありません"
            return

        self.mode = Mode.OUTPUT_LIST
        self.dir_path = self.__temp_dir
