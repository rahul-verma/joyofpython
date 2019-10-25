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

