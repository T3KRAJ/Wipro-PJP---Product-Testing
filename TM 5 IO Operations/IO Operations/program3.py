# Tek Raj Joshi
# Superset ID: 1368453

input_from_user = input("Enter the string to append: ")

with open('filename.txt', mode='a', encoding='utf-8') as f:
    f.write(input_from_user)
    f.close()
