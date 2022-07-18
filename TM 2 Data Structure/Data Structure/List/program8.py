# Tek Raj Joshi
# Superset ID: 1368453

array_of_integers = list(map(int, input("Enter the space seperated integers: ").split()))
element_to_remove = int(input("Enter the integer to remove: "))
array_of_integers.remove(element_to_remove)
print(array_of_integers)