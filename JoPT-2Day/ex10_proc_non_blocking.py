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

import requests

from jopt.file_utils import *
from jopt.project_utils import *
from jopt.process_utils import *


class Chrome:

    def __init__(self, port=4322):
        self.__port = port
        self.__base_url = 'http://localhost:{}/session'.format(self.__port)
        self.__session_id = None
        self.__session_url = None
        self.__launch_driver_process()
        self.__launch_browser()

    def __launch_driver_process(self):
        cpath = get_full_driver_path("chromedriver")
        command = [cpath, "--port={}".format(self.__port)]
        pattern = r'port\s+{}'.format(self.__port)
        try:
            launch_nonblocking_process(command, pattern)
        except Exception as e:
            raise Exception("Driver not launched: {}".format(e))

    def __launch_browser(self):
        payload = read_input_file("launch_chrome.json")
        response = requests.post(self.__base_url, payload)
        self.__session_id = response.json()['value']['sessionId']
        self.__session_url = self.__base_url + "/{}".format(self.__session_id)

    def go_to_url(self, url):
        requests.post(self.__session_url + "/url", json={'url': url})

    def get_page_source(self):
        return requests.get(self.__session_url + "/source")

    def quit(self):
        requests.delete(self.__session_url)


chrome = Chrome()
chrome.go_to_url("https://www.google.com")
response = chrome.get_page_source()
# print(response.text)
matches = re.findall(r'(<input.*?>)', response.json()['value'])
for match in matches:
    print(match)
chrome.quit()