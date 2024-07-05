#!/usr/bin/python3

import urllib.request
import sys
"""Importation of the URL library to facilitate an interface for handling
URL interface and error handling."""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

        url = sys.argv[1]

        try:
            with urllib.request.urlopen(url) as response:
                req_id = response.getheader("X-Request-Id")

            if req_id:
                print(f"X-Request-Id: {x_request_id}")
            else:
                print("X-Request-Id header not found in the response.")

        except urllib.error.URLError as e:
            print(f"URLError: {e.reason}")

        except Exception as e:
            print(f"Error: {e}")
