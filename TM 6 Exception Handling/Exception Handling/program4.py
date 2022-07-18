# Tek Raj Joshi
# Superset ID: 1368453

list_of_numbers = [-3, 4, 0, -8, -68, -88, 6, 78, 32, -46]
index = int(input("Enter the index: "))
try:
    if list_of_numbers[index] < 0:
        print("Negative Number")
    else:
        print("Positive Number")
except Exception as e:
        print("Oops!", e, "occurred.")