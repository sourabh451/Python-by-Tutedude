# to run this or before running this we have to make changes
# in project of 16REST_API's_USING_DJANGO\blog_16_2 without permission and authentication then only
# it will show all the post wrt sepcified offset or else it will give {"detail":"Authentication credentials were not provided."}
import requests
url = "http://127.0.0.1:8000/post/"

params = {
    "offset" : "10"
}

response = requests.post(url = url, params=params)

print(response.text)
print(response.url)