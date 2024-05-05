from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Firefox() # some might get error because u have not added firefox to path ie webdriver as soon as extract u have to add webdrivers path to environment variable else just add executable_path as parameter inside firefox but executable_path is deprecated you have to use an instance of the Service()
s=Service('C:/Program Files (x86)/Mozilla Firefox/geckodriver.exe')
driver = webdriver.Firefox(service=s)

driver.get('http://www.google.com')

input = driver.find_element(By.NAME, "q")
input.send_keys('selenium')
time.sleep(5)

#button = driver.find_element(By.NAME, "btnK")
button = driver.find_element(By.CLASS_NAME, "gNO89b")
button.click()



