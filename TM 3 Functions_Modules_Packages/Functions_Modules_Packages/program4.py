# Tek Raj Joshi
# Superset ID: 1368453

def get_count(str):
    upper_count, lower_count = 0, 0
    for i in str:
        if i.isalpha():
            if i.islower():
                lower_count += 1
            else:
                upper_count += 1
    return lower_count, upper_count

input_string = input("Enter a string: ")
print(get_count(input_string))