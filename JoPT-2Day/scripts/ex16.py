from jopt.process_utils import *

# For Windows use pattern: name\s+(\d+)
results = find_process_ids('(\d+)\s+\w+\s+Chrome')

print(results)
