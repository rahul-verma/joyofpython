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
wait= WebDriverWait(driver,30)

driver.get("http://18.141.139.187//wp-admin")

element = wait.until(EC.element_to_be_clickable((By.ID, 'user_login')))
element.clear()
element.send_keys('user')
assert element.get_attribute('value') == 'user'

driver.quit()