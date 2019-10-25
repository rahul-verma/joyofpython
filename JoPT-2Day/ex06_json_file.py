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

import json
import pprint

from jopt.bloglib import *
from jopt.project_utils import *


def write_json(authors, fpath):
    with open(fpath, "w") as f:
        json.dump(authors, f, indent=4)


def read_json(fpath):
    with open(fpath, "r") as f:
        output = json.load(f)
        pprint.pprint(output)


author_data = get_author_data(0,10)
file_path = get_output_file_path("authors.json")
write_json(author_data, file_path)
read_json(file_path)
