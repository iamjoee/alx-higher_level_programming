#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a specified letter as a query parameter.
Usage: ./8-json_api.py <letter>
  - The specified letter is sent as the value of the query parameter `q`.
  - If no letter is provided, the query parameter `q` is set to an empty string (`q=""`).
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
