# to run this or before running this we have to make changes
# in project of 16REST_API's_USING_DJANGO\blog_16_2 without permission and authentication then only
# it will post the details or else it will give {"detail":"Authentication credentials were not provided."}
import requests
url = "http://127.0.0.1:8000/post/"

payload = {
    "title" : "Greetings",
    "content" : "Welcome to python."
}

response = requests.post(url = url, data = payload)

print(response.text)