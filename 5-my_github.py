#!/usr/bin/python3
import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

response = requests.get('https://api.github.com/user', auth=(username, password))
print(response.json().get('id'))
