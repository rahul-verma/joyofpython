from jopt.data_utils import *

e1 = "abc@check.com"
e2 = "notanemail"

print(extract_email_parts(e1))
print(extract_email_parts(e2))