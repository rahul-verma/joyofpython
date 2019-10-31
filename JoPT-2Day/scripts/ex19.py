import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from jopt.project_utils import *

driver_path = get_driver_path("chromedriver")
driver = webdriver.Chrome(executable_path=driver_path)
wait = WebDriverWait(driver, 10)

driver.get("http://192.168.56.103/wp-admin")

element = wait.until(EC.element_to_be_clickable((By.ID, 'user_login')))
element.clear()
element.send_keys('user')
assert element.get_attribute('value') == 'user'

driver.quit()