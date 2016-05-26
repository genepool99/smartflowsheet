#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Notes: (to be in README later)
# May require pip install --upgrade ndg-httpsclient for https tls

import json
from pprint import pprint
import time
import sys
import getopt
from collections import defaultdict
import requests

class sfs:
    """Common base class for all smartflow sessions"""
    
    # This is the Production URL
    #baseURL = "https://www.smartflowsheet.com/api/v3"
    
    # This is the Sandbox URL (uncomment to use)
    baseURL = "https://sfs-public.azurewebsites.net/api/v3"

    def __init__(self, key, ckey, debug = False):
        self.key = key
        self.ckey = ckey
        self.debug = debug
        self.s = requests.session()
        
    def register_hook(self, url):
        ''' Register a custom webhook handler URL
            Method: POST
            Parameter: URL of handler
            Returns: request
        '''
        headers = {'User-Agent':'MyClient/1.0.0', 'Content-type':'application/json',  'emrApiKey':self.key, 'clinicApiKey':self.ckey}
        url = sfs.baseURL + '/account/webhook?url=' + str(url)
        try:
            r = self.s.post(url, headers=headers)
        except requests.exceptions.ConnectionError as e:
            return None
        pprint(r)
        return r
        
    def get_departments(self):
        ''' Return a list of hospital departments '''
        headers = {'User-Agent':'MyClient/1.0.0', 'Content-type':'application/json',  'emrApiKey':self.key, 'clinicApiKey':self.ckey}
        try:
            r = self.s.get(sfs.baseURL + '/departments', headers=headers, timeout=5)
            data = json.loads(r.text)
        except:
            return None
        return data
