# Tek Raj Joshi
# Superset ID: 1368453

def get_factorial(num):
    if num == 0:
        return 1
    fact = 1
    while num > 0:
        fact = fact * num
        num -= 1
    return fact
    

integer = int(input("Enter an integer: "))
print(get_factorial(integer))