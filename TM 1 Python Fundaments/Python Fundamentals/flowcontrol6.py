def checkPrime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True
num = int(input())
print(checkPrime(num))


