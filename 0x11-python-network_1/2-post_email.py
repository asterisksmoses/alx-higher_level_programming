#!/usr/bin/python3

import urllib.request
import sys
"""This script sends a POST request to an URL with an email parameter,
and to print the response content.

Arguments:
    URL: The URL to send the POST request to.
    email: The email parameter to include in the requested area.
"""

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode('ascii')
    req_x = urllib.request.Request(url, data)

    with urllib.request.urlopen(req_x) as response:
        print(response.read().decode('utf-8'))
