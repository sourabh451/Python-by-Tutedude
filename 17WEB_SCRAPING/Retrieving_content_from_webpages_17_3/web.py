# pip install urllib3
"""
import urllib.request, urllib.parse, urllib.error

url = urllib.request.urlopen("http://127.0.0.1:8000/helloworld/")

for line in url:
    print(line.decode().strip())
"""

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
"""

"""
import requests
url = "http://127.0.0.1:8000/helloworld/"
user = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
response = requests.get(url = url, headers=user)
print(response.request.headers)
"""


import requests
#url = "http://127.0.0.1:8000/helloworld/"
url = "http://127.0.0.1:8000/picture/images/nature-images.jpg"
user = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
response = requests.get(url = url, headers=user)
#print(response.content)
#print(type(response.content))
#print(response.content)
pic = response.content

f = open("nature-images.jpg","wb") #wb =writing byte
f.write(pic)