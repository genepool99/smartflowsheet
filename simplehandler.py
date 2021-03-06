#!/usr/bin/env python
#-*- coding:utf-8 -*-

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

import BaseHTTPServer
import sys
import time
import urlparse
import json


HOST_NAME = sys.argv[1]
PORT_NUMBER = int(sys.argv[2])


def handle_hook(payload):
    """ This is the actual handler for hooks """
    print payload

class HookHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """ Base class to handle hooks forked from FiloSottile/HookHandler.py"""
    server_version = "simplehandler/1.0"
    def do_GET(s):
        s.send_response(200)
        s.wfile.write('Hello! Talk post to me baby :)')

    def do_POST(s):
        # Uncomment to check that the IP is within the ranges
        #if not any(s.client_address[0].startswith(IP) for IP in ('192.168.1', '10.10.10')):
        #    s.send_error(403)

        length = int(s.headers['Content-Length'])
        content = s.rfile.read(length)
        try:
            payload = json.loads(content)
            handle_hook(payload)
            s.send_response(200)
        except ValueError, e:                   # catch bad JSON
            s.send_response(400)
            pass


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), HookHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
