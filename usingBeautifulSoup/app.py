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
    
    def crawl_profile(self, session, base_url, profile_url, post_limit)
    :
        # Goes to profile URL, crawls it and extracts posts URLs.
        profile_bs = get_bs(session, profile_url)
        n_scraped_posts = 0
        scraped_posts = list()
        posts_id = None

        while n_scraped_posts < post_limit:
            try:
                posts_id = 'recent'
                posts = profile_bs.find('div', id=posts_id).div.div.contents
            except Exception:
                posts_id = 'structured_composer_async_container'
                posts = profile_bs.find('div', id=posts_id).div.div.contents

            posts_urls = [a['href'] for a in profile_bs.find_all('a', text='Full Story')] 

            for post_url in posts_urls:
                # print(post_url)
                try:
                    post_data = scrape_post(session, base_url, post_url)
                    scraped_posts.append(post_data)
                except Exception as e:
                    logging.info('Error: {}'.format(e))
                n_scraped_posts += 1
                if posts_completed(scraped_posts, post_limit):
                    break
            
            show_more_posts_url = None
            if not posts_completed(scraped_posts, post_limit):
                show_more_posts_url = profile_bs.find('div', id=posts_id).next_sibling.a['href']
                profile_bs = get_bs(session, base_url+show_more_posts_url)
                time.sleep(3)
            else:
                break
        return scraped_posts




if __name__ == '__main__':

    fb = Facebook() # Object of class
    profiles_urls = fb.objectify('profiles_urls.json')
    credentials = fb.objectify('readme.json')

    logging.basicConfig(level=logging.INFO) #  to put some log messages on the script execution so you know what the script is actually doing
    base_url = 'https://mobile.facebook.com'
    session = requests.session()

    fb.make_login(session, base_url, credentials) # After extracting the input data from files you make the login calling

