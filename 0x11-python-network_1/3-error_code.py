#!/usr/bin/python3

import urllib.request
import sys

"""This script takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8).

Arguments:
    URL: The URL to send the POST request to.
"""

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
