import requests
import json

class ApiQuery():
    '''Class managing API queries'''
    def __init__(self, scope=1, page_size='100',
                 api_link='https://fr.openfoodfacts.org/cgi/search.pl'):
        self.page = 1
        self.scope = scope
        self.page_size = page_size
        self.payload = {'action':'process',
                        'tagtype_0':'languages',
                        'tag_contains_0':'contains',
                        'tag_0':'fr',
                        'sort_by':'unique_scans_n',
                        'json':'1',
                        'page_size':self.page_size,
                        'page':str(self.page)}
        self.api_link = api_link

    def get_query(self, output_file="resources/off_p{}_local_file.json"):
        '''Request the API and dump result in a file
        Be sure to add {} in the output_file'''

        while self.page <= self.scope:
            print("Requesting page {}".format(self.page))
            raw_output = requests.get(self.api_link, params=self.payload)
            json_output = raw_output.json()
            self.page += 1

            with open(output_file.format(str(self.page)), "w") as file:
                json.dump(json_output, file)
            print("Request output dumped in file")
