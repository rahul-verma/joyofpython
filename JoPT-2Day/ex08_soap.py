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
import xml.etree.ElementTree as etree

from jopt.file_utils import *

url = "https://www.w3schools.com/xml/tempconvert.asmx?op=CelsiusToFahrenheit"
temperature = 40

payload = read_input_file("soap_payload.xml").format(temperature)

headers = {
    'Content-Type': 'application/soap+xml'
}

response = requests.post(url, data=payload, headers=headers)
print(response.status_code)
print(response.text)
ns = {'xmlns': "https://www.w3schools.com/xml/"}
root = etree.fromstring(response.text)
for e in root.iter():
    print(e, e.tag, e.text)

temp_elem = root.find('.//xmlns:CelsiusToFahrenheitResult', ns)
result = int(temp_elem.text)
print(result)

