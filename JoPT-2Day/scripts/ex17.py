import time
import re

from selenium import webdriver

from jopt.project_utils import *

driver_path = get_driver_path("chromedriver")
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.google.com")

time.sleep(5)

matches = re.findall(r'(<input.*?>)', driver.page_source)
for match in matches:
    print(match)

driver.quit()