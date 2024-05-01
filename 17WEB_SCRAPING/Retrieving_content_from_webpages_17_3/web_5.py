# pip install bs4 #helps us to get only necessary data out of the html and xml files
# pip install lxml # helps in of easy handling of xml and html file

import requests
from bs4 import BeautifulSoup
def Extract(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')
    #tag = soup.div
    tag = soup.find('div' , {"id" : "mp-right"})
    #print(tag)
    h = tag.find("h2")
    print(h)

Extract(url="https://en.wikipedia.org/wiki/Main_Page")