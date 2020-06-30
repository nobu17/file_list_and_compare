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
    
    def create_from_csv_str(self, csv_str: str) -> PathBase:
        str_array = csv_str.split(",")
        if (len(str_array) == 1):
            return

        if (not len(str_array) == 4 and not len(str_array) == 7):
            raise Exception("file format is incorrect. len:{}".format(len(str_array)))

        try:
            path = str_array[0]
            name = str_array[1]
            created = str_array[2].strip()
            created_dt = datetime.strptime(created, "%Y/%m/%d %H:%M")
            updated = str_array[3].strip()
            updated_dt = datetime.strptime(updated, "%Y/%m/%d %H:%M")

            if (len(str_array) == 7):
                dir = str_array[4]
                extension = str_array[5]
                size = str_array[6]
                size_int = int(size)
                return File(path, name, created_dt, updated_dt, dir, extension, size_int)
            else:
                return Directory(path, name, created_dt, updated_dt)

        except Exception as e:
            print("convert error:{}".format(e))
            raise e

    @staticmethod
    def _epoch_to_datetime(epoch):
        result = datetime(*time.localtime(epoch)[:6])
        return result

