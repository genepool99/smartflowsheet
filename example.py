#!/usr/bin/env python 

from pprint import pprint
from sfs import sfs

try:
   from settings import *                       # grab passwords outside of source control
except ImportError:
   print "Setup login_setting.py before running."
   pass

## Setup enviorment
sandbox = SF_USE_SANDBOX
if sandbox:
    key = SF_SKEY
    ckey = SF_SCKEY
else:
    key = SF_PKEY
    ckey = SF_PCKEY

test = sfs(key, ckey, SF_DEBUG, SF_USE_SANDBOX)
r = test.register_hook(SF_HOOK_HANDLER)
pprint(r)
r = test.get_departments()
pprint(r)
