from jopt.data_utils import *

l1 = ['a','b','c']
l2 = 'a,b,c'
l3 = 'a#b#c'

print(convert_list_to_str(l1))
print(convert_list_to_str(l1, '#'))

print(convert_csv_str_to_list(l2))
print(convert_csv_str_to_list(l3, '#'))