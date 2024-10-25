#!/usr/bin/env python

"""
Copyright (c) 2016 tilt (https://github.com/AeonDave/doork)
See the file 'LICENSE' for copying permission
"""

import re
import requests
import time
import random
from lib.logger import logger
# from xgoogle.search import GoogleSearch, SearchError
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from googlesearch import search

def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)
        return True
    except ValidationError:
        return False

def get_html_from_url(url):

    user_agent = {'User-agent': 'Mozilla/5.0'}

    try:
        r = requests.get(url, headers = user_agent) 
        return r.content
    except Exception:
        logger.error('[-] Error: Host responded badly')
        return False
    
def scan(url, wordlist):
    
    fname = wordlist
    with open(fname, 'r') as f:
        dorks = f.readlines()
    f.close()
    for dork in dorks:
        if len(dork)<2:
            continue
        try:
            rnd = random_int(2, 5)
            time.sleep(rnd)
            g = search("Google", num_results=10, sleep_interval=10)
            #g = GoogleSearch("site:"+url+" "+dork, random_agent=True)
            #g.results_per_page = 10
            print(".")
            # results = g.get_results()
            if len(g) > 0:
                msg = "[+] Found "+ g +" results with dork: "+dork
                logger.info(msg)
                for res in g:
                    print(res.title)
                    print(res.url)
        except Exception as e:
            print("Search failed: %s" % e)
    msg = "[+] Scan finished"
    logger.info(msg)
    
def random_int(a, b):
    return(random.randint(a,b))
    
    
