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

from jopt.project_utils import *
from jopt.process_utils import *
from jopt.file_utils import *


def launch_driver_process(port):
    cpath = get_driver_path("chromedriver")
    command = [cpath, "--port={}".format(port)]
    try:
        launch_nonblocking_process(command)
    except Exception as e:
        raise Exception("Driver not launched: {}".format(e))


def launch_browser(base_url):
    payload = read_file(get_input_file_path("launch_chrome.json"))
    print(base_url)
    print(payload)
    response = requests.post(base_url, payload)
    response = response.json()
    if 'sessionId' in response:
        return response['sessionId']
    else:
        return response['value']['sessionId']


def go_to_url(session_url, url):
    requests.post(session_url + "/url", json={'url': url})


def get_page_source(session_url):
    return requests.get(session_url + "/source")


def quit(session_url):
    requests.delete(session_url)


if __name__ == "__main__":
    port=4322
    base_url = 'http://localhost:{}/session'.format(port)

    launch_driver_process(port)

    session_id = launch_browser(base_url)
    session_url = base_url + "/{}".format(session_id)

    go_to_url(session_url, "https://www.google.com")
    response = get_page_source(session_url)
    # print(response.text)
    matches = re.findall(r'(<input.*?>)', response.json()['value'])
    for match in matches:
        print(match)
    quit(session_url)