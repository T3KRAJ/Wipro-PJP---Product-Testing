# Tek Raj Joshi
# Superset ID: 1368453

input_string = input("Enter the hypen seperated sequence of colors")
color_array = input_string.split("-")
color_array = sorted(color_array)
print("-".join(color_array))