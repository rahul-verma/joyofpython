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

import unittest
import json

from selenium.webdriver.common.by import By

from jopt.driver import WebAutomator
from jopt.project_utils import *


class BaseTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__config = json.load(open(get_config_file_path(), "r"))
        self.__automator = None

    @property
    def config(self):
        return self.__config

    @property
    def automator(self):
        return self.__automator

    def __fill_login_form(self, user_name, password):
        self.automator.go_to_url(self.config["wp_url"])

        text = self.automator.set_element_text(By.ID, "user_login", user_name)
        self.assertEqual(user_name, text, "Expected text not entered in user name field.")

        text = self.automator.set_element_text(By.ID, "user_pass", password)
        self.assertEqual(password, text, "Expected text not entered in password field.")

        self.automator.click_element(By.ID, "wp-submit")

    def login_with_valid_creds(self, user_name, password):
        self.__fill_login_form(user_name, password)
        try:
            self.automator.wait_until_present(By.XPATH, "//*[text()='WordPress News']")
        except Exception as e:
            raise AssertionError("Login not successful: {}".format(e))

    def login_with_invalid_creds(self, user_name, password, message):
        self.__fill_login_form(user_name, password)
        error_div = self.automator.wait_until_present(By.ID, "login_error")
        self.assertIn(message, error_div.text, "Expected error message not seen.")

    def logout(self):
        logout_link = self.automator.wait_until_present(By.XPATH,"//*[text()='Log Out']")
        self.automator.go_to_url(logout_link.get_attribute("href"))
        self.automator.wait_until_present(By.XPATH, "//*[contains(text(),'logged out')]")

    def setUp(self):
        self.__automator = WebAutomator()

    def tearDown(self):
        self.automator.quit()


'''
    # For class level fixtures

    __automator = None
    
    @property
    def automator(self):
        return self.__class__.__automator

    @classmethod
    def setUpClass(cls):
        cls.__automator = WebAutomator()

    @classmethod
    def tearDownClass(cls):
        cls.__automator.quit()

'''