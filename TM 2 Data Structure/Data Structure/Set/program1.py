# Tek Raj Joshi
# Superset ID: 1368453

set_of_integers = set(map(int, input("Enter the space seperated integers: ").split()))
elem_to_remove = int(input("Enter the element you want to remove: "))
set_of_integers.remove(elem_to_remove)
print(set_of_integers)