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
from ddt import ddt, data
from jopt.basetest import BaseTest

@ddt
class LoginTest(BaseTest):

    def test_valid_login(self):
        user_name = self.config["wp_user"]
        password = self.config["wp_pwd"]
        self.login_with_valid_creds(user_name, password)
        self.logout()

    @data(
        ('anything', 'any_pass', 'Invalid username'),
        ('user', 'wrong_pass', r'The password you entered for the username {} is incorrect')
    )
    def test_invalid_login(self, data):
        user_name, password, message = data
        try:
            message = message.format(user_name)
        except Exception:
            pass
        self.login_with_invalid_creds(user_name, password, message)


if __name__ == "__main__":
    unittest.main()
