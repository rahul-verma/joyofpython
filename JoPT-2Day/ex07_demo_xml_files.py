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

import pprint
from xml.etree import ElementTree as etree
from xml.dom import minidom

from jopt.bloglib import *
from jopt.project_utils import *


def __get_author_values(in_data):
    return {k:str(v) for k,v in in_data.items()}


def write_xml(authors, fpath):
    with open(fpath, "w") as f:
        root = etree.Element('authors')
        for author in authors:
            etree.SubElement(root, 'author', __get_author_values(author))
        output = etree.tostring(root, encoding="unicode")

        # Trick from https://pymotw.com/2/xml/etree/ElementTree/create.html#pretty-printing-xml
        reparsed = minidom.parseString(output)
        f.write(reparsed.toprettyxml(indent="   "))


def read_xml(fpath):
    tree = etree.parse(fpath)
    root = tree.getroot()
    output = []
    for elem in root.iter():
        if elem.tag == 'author':
            output.append(elem.attrib)
    pprint.pprint(output)


author_data = get_author_data(0,10)
file_path = get_output_file_path("authors.xml")
write_xml(author_data, file_path)
read_xml(file_path)
