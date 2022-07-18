# Tek Raj Joshi
# Superset ID: 1368453

import sys

first_string = sys.argv[1].split('-')
second_string = sys.argv[2].split('-')
third_string = sys.argv[3].split('-')

add = [i for i in first_string if i in third_string]
minus = [i for i in second_string if i in third_string]

print("happiness is: ", len(add) - len(minus))