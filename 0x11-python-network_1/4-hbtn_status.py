#!/usr/bin/python3

import requests
"""This script  fetches https://alx-intranet.hbtn.io/status."""

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url)
    if resp.status_code == 200:
        print("Body:", resp.text)
    else:
        print("Error code:", resp.status_code)
