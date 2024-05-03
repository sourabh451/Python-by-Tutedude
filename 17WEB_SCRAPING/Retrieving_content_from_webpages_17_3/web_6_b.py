import requests
import re
user = input("Enter the image name: ")
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
url = f"https://www.google.com/search?q={user}&tbm=isch"
response = requests.get(url=url, headers=user_agent).text
pattern = 'https://.*?\.jpg'
images = re.findall(pattern, response)
print(f"Total Images : {len(images)}")
no_of_images = int(input("Number of images to be downloaded: "))

if images:
    for image_url in images[:no_of_images]:
        #print(image_url)
        #print(type(image_url))
        #image_url = eval(image)[0]
        response = requests.get(url= image_url).content
        print(response)