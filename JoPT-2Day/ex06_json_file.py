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
