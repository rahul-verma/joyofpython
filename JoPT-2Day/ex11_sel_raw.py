import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from jopt.project_utils import *

driver_path = get_full_driver_path("chromedriver")
chrome = webdriver.chrome(executable_path=driver_path)

chrome.get("http://192.168.56.103/wp-admin")

time.sleep(5)

user_textbox = chrome.find_element(By.ID, "user_login")
user_textbox.send_keys("user")

password_textbox = chrome.find_element(By.ID, "user_pass")
password_textbox.send_keys("bitnami")

chrome.find_element(By.ID, "wp-submit").click()