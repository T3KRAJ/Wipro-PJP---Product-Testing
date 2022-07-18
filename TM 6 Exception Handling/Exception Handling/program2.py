# Tek Raj Joshi
# Superset ID: 1368453

def checkPrime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

try:
    num = input("Enter the number: ")
    print(checkPrime(int(num)))
except Exception as e:
        print("Oops!", e, "occurred.")