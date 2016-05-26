#!/usr/bin/env python 

from pprint import pprint
from sfs import sfs

try:
   from login_settings import *                       # grab passwords outside of sorce control
except ImportError:
   print "Setup login_setting.py before running."
   pass

##
# Set Global Constants
##
SF_DEBUG = False                            
##

test = sfs(SF_SKEY, SF_SCKEY, SF_DEBUG)
#r = test.register_hook('http://104.131.150.244:9999')
r = test.get_departments()
pprint(r)
