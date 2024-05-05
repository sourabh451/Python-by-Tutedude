from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://www.amazon.in')
driver.maximize_window()

time.sleep(5)

select = driver.find_element(By.LINK_TEXT,"Electronics")
select.click()

time.sleep(5)

select_1 = driver.find_element(By.LINK_TEXT,"Audio")
select_1.click()