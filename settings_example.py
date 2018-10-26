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
# This is the secerets file, keep untracked by source control
# rename settings.py and save in script root directory

SF_USERNAME = "example@domain.com"                          # website login
SF_PASSWORD = "mypassword"                                  # website password
SF_DEBUG = False                                            # debugging on/off default = False
SF_PKEY = "your production api key"                         # PRODUCTION API Key
SF_PCKEY = "your production clinic key"                     # PRODUCTION Clinic API Key
SF_SKEY = "your sandbox api key"                            # SANDBOX API Key
SF_SCKEY = "your sandbox clinic key"                        # SANDBOX Clinic API Key
SF_USE_SANDBOX = True                                       # Switch between sandbox and production
SF_HOOK_HANDLER = 'yourHandlerURL'                          # the url to setup a webhook handler
