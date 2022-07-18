initial = int(input())
res = 0
num = initial
while num > 0:
    rem = num % 10
    res = res * 10 + rem
    num //= 10
print(num)
print(res)

if initial == res:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")
