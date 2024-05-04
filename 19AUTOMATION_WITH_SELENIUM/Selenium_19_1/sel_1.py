#  pip install selenium
#  download firefox webdirver from https://github.com/mozilla/geckodriver/releases as per firefox version and extract in C:\Program Files (x86)\Mozilla Firefox

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#driver = webdriver.Firefox() # some might get error because u have not added firefox to path ie webdriver as soon as extract u have to add webdrivers path to environment variable else just add executable_path as parameter inside firefox but executable_path is deprecated you have to use an instance of the Service()
s=Service('C:/Program Files (x86)/Mozilla Firefox/geckodriver.exe')
driver = webdriver.Firefox(service=s)

driver.get('http://www.google.com')