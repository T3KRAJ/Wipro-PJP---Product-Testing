# Tek Raj Joshi
# Superset ID: 1368453

def check_prime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

num = int(input())
print(check_prime(num))
