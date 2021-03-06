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

import os

from .os_utils import *

def get_root_dir():
    my_dir = os.path.realpath(os.path.dirname(__file__))
    return os.path.abspath(os.path.join(my_dir, ".."))


def get_input_file_path(file_name):
    return os.path.join(get_root_dir(), "input", file_name)


def get_output_file_path(file_name):
    dir_path = os.path.join(get_root_dir(), "output")
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    return os.path.join(dir_path, file_name)


def get_driver_path(driver_name):
    if is_windows_os(): driver_name += '.exe'
    return os.path.join(get_root_dir(), "drivers", driver_name)


def get_config_file_path():
    return os.path.join(get_root_dir(), "config", "config.json")