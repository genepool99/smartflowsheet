# smartflowsheet
## A Python 2 implementation of the Smart Flow Sheet API
More information visit: http://veterinarium.github.io/

# License
Copyright (C) 2018 - DoveLewis
Author: Avi Solomon (asolomon@dovelewis.org)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

###Notes:
Before starting, create a `setting.py` in the project directory using the example in `setting_example.py`. Then check out `examples.py`, just uncomment the API call you want to test.

If you encounter https tls errors you may need to upgrade
  ```pip install --upgrade ndg-httpsclient for https tls```

Ubuntu and Debian may also require the additional packages:
  ```apt-get install libffi-dev libssl-dev```
