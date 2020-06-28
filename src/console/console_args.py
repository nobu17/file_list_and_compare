class ConsoleArgs:

    def __init__(self, args):
        self.args = args
        self._init_variable()
        self.check_args()
        if(self.isvalid):
            self._set_param_from_args(args)

    def _init_variable(self):
        self.isvalid = True
        self.errormessage = ""
        self.dir_path = ""

    def check_args(self):
        # check length
        # print("length is {}".format(len(self.args)))
        if(len(self.args) < 2):
            self.isvalid = False
            self.errormessage = "引数がありません。"

    def _set_param_from_args(self, args):
        self.dir_path = args[1]
