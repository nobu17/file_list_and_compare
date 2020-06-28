import glob
import os
import datetime
from typing import List
from domains.models.path_service import AbstractPathRepository
from domains.models.path import PathBase


class OSPathRepository(AbstractPathRepository):

    def findAll(self, path: str) -> List[PathBase]:
        # for prob, add * mark
        plob_path = path
        if(path.endswith("/")):
            prob_path = path + "*"
        else:
            prob_path = path + "/*"

        print("target path:{}".format(prob_path))

        file_list = []
        file_str_list = glob.glob(prob_path)
        for file_str in file_str_list:
            print(file_str)
            file = self.factory.create(file_str)
            file_list.append(file)

        return file_list

    def save(self, paths: List[PathBase]):
        csv_str = ""
        for path in paths:
            csv_str += path.to_csv_str() + '\n'

        dir = os.getcwd()
        file_name = datetime.date.today().strftime('%Y%m%d%H%M%s') + ".csv"
        file_path = dir + "/" + file_name
        with open(file_path, mode='w') as f:
            f.write(csv_str)

    def load(self, setting_path: str) -> List[PathBase]:
        pass
