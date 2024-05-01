# pip install bs4 #helps us to get only necessary data out of the html and xml files
# pip install lxml # helps in of easy handling of xml and html file

import requests
from bs4 import BeautifulSoup
import csv
def Extract(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')
    #tag = soup.div
    tag = soup.find('div' , {"id" : "mp-right"})
    #print(tag)
    #h = tag.find("h2")
    #h = tag.find("h2").find("span")
    h = tag.find_all("h2")
    #print(h)
    content = [span.text for span in h]
    #print(content)

    with open("wiki.csv","w") as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(content)

Extract(url="https://en.wikipedia.org/wiki/Main_Page")