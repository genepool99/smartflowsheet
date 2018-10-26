#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2018 - DoveLewis
# Author: Avi Solomon (asolomon@dovelewis.org)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
    baseProductionURL = "https://www.smartflowsheet.com/api/v3"

    # This is the Sandbox URL (uncomment to use)
    baseSandboxURL = "https://sfs-public.azurewebsites.net/api/v3"

    def __init__(self, key, ckey, debug, sandbox):
        self.key = key
        self.ckey = ckey
        self.debug = debug
        self.s = requests.session()
        if sandbox:
            self.baseURL = self.baseSandboxURL
        else:
            self.baseURL = self.baseProductionURL

    def register_hook(self, url):
        ''' Register a custom webhook handler URL
            Method: POST
            Parameter: URL of handler
            Returns: request
        '''
        headers = {'User-Agent':'MyClient/1.0.0', 'Content-type':'application/json',  'emrApiKey':self.key, 'clinicApiKey':self.ckey}
        url = self.baseURL + '/account/webhook?url=' + str(url)
        try:
            r = self.s.post(url, headers=headers)
        except requests.exceptions.ConnectionError as e:
            return None
        pprint(r)
        return r

    def get_departments(self):
        ''' Return a dictionary of hospital departments '''
        headers = {'User-Agent':'MyClient/1.0.0', 'Content-type':'application/json',  'emrApiKey':self.key, 'clinicApiKey':self.ckey}
        try:
            r = self.s.get(self.baseURL + '/departments', headers=headers, timeout=5)
            data = json.loads(r.text)
        except:
            return None
        return data

    def get_active_hosp(self):
        ''' Return a dictionary of active hospiltaizations '''
        headers = {'User-Agent':'MyClient/1.0.0', 'Content-type':'application/json',  'emrApiKey':self.key, 'clinicApiKey':self.ckey}
        try:
            r = self.s.get(self.baseURL + '/hospitalizations', headers=headers, timeout=5)
            data = json.loads(r.text)
        except:
            return None
        return data

    def get_hosp(self, hid):
        ''' Return a hospiltaization object or None '''
        headers = {'User-Agent':'MyClient/1.0.0', 'Content-type':'application/json',  'emrApiKey':self.key, 'clinicApiKey':self.ckey}
        try:
            url = self.baseURL + '/hospitalization/' + str(hid)
            print url
            r = self.s.get(url, headers=headers, timeout=5)
            data = json.loads(r.text)
        except:
            return None
        return data
