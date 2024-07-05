#!/usr/bin/python3

import urllib.request
import urllib.error
"""Importation of the urllib module that provides a simple
interface for handling URL and error handling."""

url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url) as r:
            part = r.read()

            decoded_part = part.decode('utf-8')

    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")

    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

    except Exception as e:
        print(f"Error: {e}")
