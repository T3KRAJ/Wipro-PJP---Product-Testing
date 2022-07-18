# Tek Raj Joshi
# Superset ID: 1368453

input_string = input("Enter a string: ")
upper_count, lower_count = 0, 0
for i in input_string:
    if i.islower():
        lower_count += 1
    else:
        upper_count += 1

print(upper_count, lower_count)