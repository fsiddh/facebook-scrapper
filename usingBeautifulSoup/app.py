import requests
import re
import json
import time
import logging
import pandas
from collections import OrderedDict
from bs4 import BeautifulSoup

class Facebook:

    # Extracting your json from a json file
    def objectify(self, json_file):
        objct = None
        with open(json_file) as json_f:
            objct = json.loads(json_f.read())
        return objct

    def make_login(self, session, base_url, credentials):

        # Returns a Session object logged in with credentials.
        login_form_url = '/login/device-based/regular/login/?refsrc=https%3A'\
            '%2F%2Fmobile.facebook.com%2Flogin%2Fdevice-based%2Fedit-user%2F&lwv=100'

        params = {'email':credentials['email'], 'pass':credentials['pass']}

        while True:
            time.sleep(3)
            logged_request = session.post(base_url+login_form_url, data=params)
            
            if logged_request.ok:
                logging.info('[*] Logged in.')
                break



if __name__ == '__main__':

    fb = Facebook() # Object of class
    profiles_urls = fb.objectify('profiles_urls.json')
    credentials = fb.objectify('readme.json')

    logging.basicConfig(level=logging.INFO) #  to put some log messages on the script execution so you know what the script is actually doing
    base_url = 'https://mobile.facebook.com'
    session = requests.session()

    fb.make_login(session, base_url, credentials) # After extracting the input data from files you make the login calling

    