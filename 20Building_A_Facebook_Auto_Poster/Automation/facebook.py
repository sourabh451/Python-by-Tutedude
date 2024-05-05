from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://facebook.com')
emailelement = driver.find_element(By.XPATH,'.//*[@id="email"]')
emailelement.send_keys('sours901@gmail.com')
passelement = driver.find_element(By.XPATH,'.//*[@id="pass"]')
passelement.send_keys('asdfg123')

elem = driver.find_element(By.NAME,'login')
elem.click()

time.sleep(5)
boxelement = driver.find_element(By.XPATH,'./html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span')
boxelement.click()

#statuselement = driver.find_element(By.XPATH,'./html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]')
#time.sleep(5)
#statuselement.send_keys('Hi There')

time.sleep(5)
postarea = driver.find_element(By.XPATH, './/*[@class="_6s5d _71pn system-fonts--body segoe"]')
time.sleep(5)
postarea.send_keys('Hi There')


buttons = driver.find_elements(By.TAG_NAME,'span')
time.sleep(5)

for button in buttons:
    if button.text == 'Post':
        button.click()

