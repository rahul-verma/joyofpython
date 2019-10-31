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
import json

from jopt.bloglib import *
from jopt.project_utils import *
from jopt.data_utils import *


# Given a dict create a list of values for keys passed in attrs
def __get_author_values(in_data, attrs):
    out = []
    for attr in attrs:
        out.append(str(in_data[attr]))
    return out


def __write_line(file_handle, line_parts, delimiter):
    file_handle.write(convert_list_to_str(line_parts, delimiter) + '\n')


def write_csv(authors, attrs, fpath, delimiter=","):
    with open(fpath, "w") as f:
        __write_line(f, attrs, delimiter)
        for author in authors:
            __write_line(f, __get_author_values(author, attrs), delimiter)


def read_csv(fpath, delimiter=","):
    output = []
    with open(fpath, "r") as f:
        headers = f.readline().strip().split(delimiter)
        for line in f.readlines():
            line = line.strip()
            record = convert_to_map(headers, convert_csv_str_to_list(line, delimiter))
            output.append(record)
    #pprint.pprint(output)
    return output

########################################################


def write_json(authors, fpath):
    with open(fpath, "w") as f:
        json.dump(authors, f, indent=4)


def read_json(fpath):
    output = None
    with open(fpath, "r") as f:
        output = json.load(f)
    #pprint.pprint(output)
    return output


if __name__ == "__main__":
    author_data = get_author_data(0, 10)

    attrs = author_data[0].keys()
    file_path = get_output_file_path("authors.csv")
    write_csv(author_data, attrs, file_path)

    csv_output = read_csv(file_path)

    file_path = get_output_file_path("authors.json")
    write_json(author_data, file_path)
    json_output = read_json(file_path)

    # Not efficient. Kept here only for simplicity of logic sake.

    for entry in csv_output:
        for jentry in json_output:
            if int(entry['id']) == jentry['id']:
                assert entry['username'] == jentry['username']
                break
