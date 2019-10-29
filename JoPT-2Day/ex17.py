import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By

from jopt.project_utils import *

driver_path = get_driver_path("chromedriver")
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("http://192.168.56.103/wp-admin")

time.sleep(5)

matches = re.findall(r'(<input.*?>)', driver.page_source)
for match in matches:
    print(match)

driver.quit()