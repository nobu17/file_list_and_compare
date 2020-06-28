import os
import time
from pathlib import Path
from datetime import datetime
from domains.models.path_factory import AbstractPathFactory
from domains.models.path import PathBase, Directory, File

class OSPathFactory(AbstractPathFactory):

    def create(self, path: str) -> PathBase:
        p = Path(path)
        if(not p.exists()):
            raise Exception("{} is not existed.".format(path))

        created = OSPathFactory._epoch_to_datetime(os.path.getctime(p))
        updated = OSPathFactory._epoch_to_datetime(os.path.getmtime(p))

        if(p.is_file()):
            file = File(path, p.name, created, updated, str(p.parent), ''.join(p.suffixes), os.path.getsize(path))
            return file
        else:
            dir = Directory(path, p.name, created, updated)
            return dir

    @staticmethod
    def _epoch_to_datetime(epoch):
        result = datetime(*time.localtime(epoch)[:6])
        return result
