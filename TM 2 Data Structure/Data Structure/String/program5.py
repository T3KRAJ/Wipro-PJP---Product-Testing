# Tek Raj Joshi
# Superset ID: 1368453

input_string = input("Enter a string: ")
n = int(input("Enter n: "))
res = ''
for i in range(n):
    res += input_string[-n: ]
print(res)