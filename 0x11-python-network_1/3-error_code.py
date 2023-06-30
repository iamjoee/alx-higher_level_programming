#!/usr/bin/python3
"""A script that:
- accepts a URL as input
- sends a request to the specified URL
- displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
