#!/usr/bin/python3
"""Fetches basic request with urlib"""
from urllib import requests

with requests.urlopen("https://intranet.hbtn.io/status") as response:
    r = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(r), r, r.decode('utf-8')))