import time
import re

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

driver.get("https://www.google.com")

time.sleep(5)

matches = re.findall(r'(<input.*?>)', driver.page_source)
for match in matches:
    print(match)

driver.quit()