from jopt.project_utils import *


def read_input_file(file_name):
    f = open(get_input_file_path(file_name))
    content = f.read()
    f.close()
    return content
