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


import re


def convert_list_to_str(in_list, delimiter=','):
    return delimiter.join([str(i) for i in in_list])


def convert_csv_str_to_list(csv_str, delimiter=','):
    return csv_str.split(delimiter)


def convert_to_map(seq1, seq2):
    return dict(zip(seq1, seq2))


def extract_email_parts(email_address):
    pattern = r'(\w+)@(.*)'
    match = re.match(pattern, email_address)
    if match:
        return match.groups()
    else:
        raise Exception("{} is not an email".format(email_address))
