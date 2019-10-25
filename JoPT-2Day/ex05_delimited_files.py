import pprint

from jopt.bloglib import *
from jopt.project_utils import *


# Given a dict create a list of values for keys passed in attrs
def __get_author_values(in_data, attrs):
    out = []
    for attr in attrs:
        out.append(str(in_data[attr]))
    return out


def __write_line(file_handle, line_parts, delimiter):
    file_handle.write(delimiter.join(line_parts) + os.linesep)


def write_csv(authors, attrs, fpath, delimiter=","):
    with open(fpath, "w") as f:
        __write_line(f, attrs, delimiter)
        for author in authors:
            __write_line(f, __get_author_values(author, attrs), delimiter)


def read_csv(fpath, delimiter=","):
    with open(fpath, "r") as f:
        output = []
        headers = f.readline().strip().split(delimiter)
        for line in f.readlines():
            line = line.strip()
            record = dict(zip(headers, line.split(delimiter)))
            output.append(record)
        pprint.pprint(output)


author_data = get_author_data(0,10)
attrs = author_data[0].keys()
file_path = get_output_file_path("authors.csv")
write_csv(author_data, attrs, file_path)
read_csv(file_path)
