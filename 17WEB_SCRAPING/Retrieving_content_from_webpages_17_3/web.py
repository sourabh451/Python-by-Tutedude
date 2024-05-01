# pip install urllib3
"""
import urllib.request, urllib.parse, urllib.error

url = urllib.request.urlopen("http://127.0.0.1:8000/helloworld/")

for line in url:
    print(line.decode().strip())
"""

# pip install requests

import requests

url = "http://127.0.0.1:8000/helloworld/"

#print(dir(requests))
response = requests.get(url = url)
print(response)
print(dir(response))
print(response.status_code)
print(response.headers)
print(response.request.headers)