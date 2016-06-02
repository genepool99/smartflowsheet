#!/usr/bin/env python 

from pprint import pprint
from sfs import sfs

try:
   from settings import *                       # grab passwords/keys outside of source control
except ImportError:
   print "Setup login_setting.py before running."
   pass

## Setup env
sandbox = SF_USE_SANDBOX
if sandbox:
    key = SF_SKEY
    ckey = SF_SCKEY
else:
    key = SF_PKEY
    ckey = SF_PCKEY

test = sfs(key, ckey, SF_DEBUG, sandbox)

## Register a new webhook handler
r = test.register_hook(SF_HOOK_HANDLER)
pprint(r)

## Get the clinic departments 
r = test.get_departments()
pprint(r)

## Get active hospitalizations
r = test.get_active_hosp()
pprint(r)

## Get a specific hospitalization
r = test.get_hosp('INSERT HOSP ID')
pprint(r)
