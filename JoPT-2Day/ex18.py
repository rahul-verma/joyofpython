import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from jopt.project_utils import *

driver_path = get_driver_path("chromedriver")
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("http://192.168.56.103/wp-admin")

time.sleep(5)

element = driver.find_element(By.ID, 'user_login')
print(element.get_attribute("outerHTML"))
element = driver.find_element(By.NAME, 'log')
print(element.get_attribute("outerHTML"))
element = driver.find_element(By.XPATH, '//*[@id="user_login"]')
print(element.get_attribute("outerHTML"))
element = driver.find_element(By.CSS_SELECTOR, '#user_login')
print(element.get_attribute("outerHTML"))

driver.quit()