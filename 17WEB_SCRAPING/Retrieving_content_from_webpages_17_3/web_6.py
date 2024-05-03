import requests
import re

user = input("Enter the image name: ")

user_agent = {
    "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
url = f"https://www.google.com/search?sca_esv=450a9a9b983914d8&sxsrf=ACQVn0__adjDE93ghjaoFfM8i9gxgORnQg:1714569588116&q={user}&uds=AMwkrPuOzfHW47FsQBhXV8rx0VyLsuGpbfE881Wx3U5JO9VG7rHfs9Ah6EfWvTERlEnwEuAPNodB7Tu1njaNPt6jHVFYNbmBbM9q7Db4wruU6-bMk3tLizdjTFJIjyYxDVbCZrb14x_shTQ9N4PWhLcdxNk9_TxKy3Zvrth-m1M2ofaAc9eA7wVjg4oZ9U-uJTY0I95R9758AGLunhA97trQSnFuqYf_wgII56GiX4HOjf9hXHvwkxEqqKsmiQO-jsnskP4QKyx5wFvihvqMRFvRCWplwwTCpB-EUcUgXkEQ8jfoeK_U0Uw&udm=2&prmd=invsmbtz&sa=X&ved=2ahUKEwj81_e5xeyFAxWAcGwGHWL_DeEQtKgLegQIDRAB&biw=1163&bih=539&dpr=1.65"

response = requests.get(url = url, headers=user_agent).text

#print(response)

pattern = "\[\"https://.*\.jpg\",[0-9]+,[0-9]+\]"

images = re.findall(pattern, response)

#print(images)
for image in images:
    print(image)
    #print(type(image))
    #image_url = eval(image)[0]
    #print(image_url)

#["https://earthsky.org/upl/2023/01/Moon-Apogee-Perigee-Niveth-Kumar-12-8-2022-800x706.jpg",706,800]
