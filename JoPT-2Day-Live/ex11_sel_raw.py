'''
This file is a part of The Joy of Python Gihub Repository.
Copyright 2019 Rahul Verma
Website: www.RahulVerma.net
Email: rv [at] testmile.com
Creator: Rahul Verma
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

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