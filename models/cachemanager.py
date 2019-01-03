import json
import os

class CacheManager():
    '''A cache manager'''
    def __init__(self, directory="resources/"):
        self.cache_dir = directory
        self.file_available = list()

    @property
    def assert_cache(self):
        '''Return a tuple (True, number_of_file_in_dir)
        if there is file in self.cache_dir ; else return False'''

        with os.scandir(self.cache_dir) as filelist:
            for entry in filelist:
                if entry.is_file():
                    if entry.name not in self.file_available:
                        self.file_available.append(entry.name)
        check = bool(self.file_available)

        return check

    def load_cache(self):
        '''Return a list of json dict object from self.cache_dir'''

        print("Loading cached files")
        files_output = list()
        for file in self.file_available:
            # print("{}{}".format(self.cache_dir, file))
            with open("{}{}".format(self.cache_dir, file), "r") as current_file:
                output = json.load(current_file)
                files_output.append(output)

        return files_output
