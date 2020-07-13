import glob
import os
import datetime
from typing import List
from domains.models.path_repository import AbstractPathRepository
from domains.models.path import PathBase
from domains.services.path_service import CompareResults, CompareInfo


class OSPathRepository(AbstractPathRepository):

    def findAll(self, path: str) -> List[PathBase]:
        # for prob, add * mark
        plob_path = path
        if(path.endswith("/")):
            prob_path = path + "**"
        else:
            prob_path = path + "/**"

        print("target path:{}".format(prob_path))

        file_list = []
        file_str_list = glob.glob(prob_path, recursive=True)
        for file_str in file_str_list:
            print(file_str)
            file = self.factory.create(file_str)
            file_list.append(file)

        return file_list

    def find(self, path: str) -> PathBase:
        file = self.factory.create(path)
        return file

    def save(self, paths: List[PathBase]):
        # add a header
        csv_str = PathBase.get_csv_header_str() + '\n'
        for path in paths:
            csv_str += path.to_csv_str() + '\n'

        dir = os.getcwd()
        file_name = datetime.date.today().strftime('%Y%m%d%H%M%s') + ".csv"
        file_path = dir + "/" + file_name
        with open(file_path, mode='w') as f:
            f.write(csv_str)

    def save_compare_result(self, result: CompareResults):
        csv_str = f'success:{result.success_count},fail:{result.fail_count}\n'
        # add a header
        csv_str += CompareInfo.get_csv_header_str() + '\n'
        for res in result.results:
            csv_str += res.to_csv_str() + '\n'

        dir = os.getcwd()
        file_name = datetime.date.today().strftime(
            '%Y%m%d%H%M%s') + "_compare_result.csv"
        file_path = dir + "/" + file_name

        with open(file_path, mode='w') as f:
            f.write(csv_str)

    def load(self, setting_path: str) -> List[PathBase]:
        files_list = []
        line_num = 0
        with open(setting_path) as f:
            while True:
                try:
                    line_num += 1
                    line = f.readline().rstrip('\n')
                    # skip a header
                    if(line_num == 1):
                        continue
                    if(len(line) != 0):
                        files_list.append(
                            self.factory.create_from_csv_str(line))
                    if not line:
                        break
                except Exception as e:
                    print("Error:{}".format(e))
                    message = f'Parse error from CSV file. LineNo:{line_num}, Str:{line}'
                    raise Exception(message) from e

        return files_list
