#!/usr/bin/python3
"""
    this module fetches `https://alx-intranet.hbtn.io/status`
"""
from urlib.request import urlopen


if__name__ == "__main__":
    """prevents from being executed"""
    with urlopen("https://alx-intranet.htbn.io/status") as response:
        html = response.read()

    print('Body response:')
    print('\t- type:', type(html))
    print('\t- content:', html)
    print('\t- utf8 content:', html.decode('utf-8'))
