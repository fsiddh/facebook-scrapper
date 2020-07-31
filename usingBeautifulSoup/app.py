import request
from bs4 import BeautifulSoup

class Facebook:

    def get_credentials():
    config_data = None
    with open('readme.json') as json_file:
        config_data = json.load(json_file)
    return config_data['facebook']    

    