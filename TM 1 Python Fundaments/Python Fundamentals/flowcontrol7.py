def checkPrime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return
    return num
for i in range(10, 99):
    if i % 2 != 0:
        res = checkPrime(i)
        if res:
            print(res)
