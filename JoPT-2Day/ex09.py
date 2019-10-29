from jopt.file_utils import *
from jopt.project_utils import *

content = "This is a test string"
file_path = get_output_file_path("test.txt")

write_file(file_path, content)
read_content = read_file(file_path)

assert read_content == content