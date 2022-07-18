def lastDigit(n1, n2):
    if n1%10 == n2%10:
        return True
    else:
        return False

num1 = int(input())
num2 = int(input())
print(lastDigit(num1, num2))