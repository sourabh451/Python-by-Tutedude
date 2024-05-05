from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://www.amazon.in')
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys('iphones')
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()

list = driver.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")

# 00 products found
print(str(len(list)) + 'products found')

for i in list:
    print(i.text)

driver.quit()