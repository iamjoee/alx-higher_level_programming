#!/usr/bin/python3
"""A script that:
- accepts a URL and an email address as inputs
- sends a POST request to the provided URL with the email as a parameter
- displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
