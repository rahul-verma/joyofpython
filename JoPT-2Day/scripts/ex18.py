import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from jopt.project_utils import *

driver_path = ChromeDriverManager().install()
svc = Service(driver_path)
svc.start()
driver = webdriver.Remote(svc.service_url)

driver.get("http://18.141.139.187/wp-admin")

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