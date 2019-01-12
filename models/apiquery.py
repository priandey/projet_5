'''Module importing json from api and saving it in cache'''
import json

import requests

class ApiQuery():
    '''Class managing API queries'''
    def __init__(self, scope=1, page_size='1000',
                 api_link='https://fr.openfoodfacts.org/cgi/search.pl'):
        self.page = 1
        self.scope = scope
        self.page_size = page_size
        self.category = ['aliments-et-boissons-a-base-de-vegetaux',
                         'boissons',
                         'plats-prepares',
                         'produits-laitiers',
                         'snacks-sucres',
                         'viandes'
                         ]
        self.payload = {'action':'process',
                        'tagtype_0':'languages',
                        'tag_contains_0':'contains',
                        'tag_0':'fr',
                        'tagtype_1':'categories',
                        'tag_contains_1':'contains',
                        'tag_1': '',
                        'sort_by':'unique_scans_n',
                        'json':'1',
                        'page_size':self.page_size,
                        'page':str(self.page)}
        self.api_link = api_link

    def get_query(self, output_file="resources/off_{}_p{}_local_file.json"):
        '''Request the API and dump result in a file
        Be sure to add 2*{} in the output file name'''
        for category in self.category:
            self.payload['tag_1'] = category
            self.page = 1
            while self.page <= self.scope:
                print("Requesting page {} ({} entries) of cat:{}".\
                                    format(self.page, self.page_size, category))
                raw_output = requests.get(self.api_link, params=self.payload)
                json_output = raw_output.json()

                with open(output_file.format(category, str(self.page)), "w") as file:
                    json.dump(json_output, file)

                self.page += 1
                print("Request output dumped in file")
