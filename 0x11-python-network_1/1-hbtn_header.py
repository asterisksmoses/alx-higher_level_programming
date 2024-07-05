#!/usr/bin/python3

import urllib.request
import sys
"""Importation of the URL library to facilitate an interface for handling
URL interface and error handling."""

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
