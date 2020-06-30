
from enum import Enum
from pathlib import Path


class Mode(Enum):
    OUTPUT_LIST = 1
    COMPARE_FROM_FILE = 2


class ConsoleArgs:

    def __init__(self, args):
        self.args = args
        self._init_variable()
        self.check_args()

    def _init_variable(self):
        self.isvalid = True
        self.errormessage = ""
        self.dir_path = ""
        self.compare_file_list_path = ""
        self.mode = Mode.OUTPUT_LIST

    def check_args(self):
        if(len(self.args) < 2):
            self.isvalid = False
            self.errormessage = "引数がありません。"
            return

        # check mode
        param = self.args[1]
        p = Path(param)
        if (p.is_file() and ''.join(p.suffixes).lower() == ".csv"):
            self.mode = Mode.COMPARE_FROM_FILE
            self.compare_file_list_path = param
            return

        if (not p.is_dir()):
            self.isvalid = False
            self.errormessage = "指定されたファイルはフォルダではありません"
            return

        self.mode = Mode.OUTPUT_LIST
        self.dir_path = param
