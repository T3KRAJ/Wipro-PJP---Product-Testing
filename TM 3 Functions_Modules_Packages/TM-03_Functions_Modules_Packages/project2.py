# Tek Raj Joshi
# Superset ID: 1368453

from collections import Counter

def is_palindrome(name):
    if name[::-1] == name:
        return "Yes it is a palindrome"
    else:
        return "No it is not a palindrome"


def vowels_count(name):
    count=0
    for i in name:
        if i in "aeiouAEIOU":
            count += 1
    print("No of vowels: ", end="")
    return count

def frequency_of_letters(name):
    frequency = Counter(name)
    print("Frequency of Letters: ", end="")
    return frequency
        
name= input("Enter the name: ")

print(is_palindrome(name))
print(vowels_count(name))
print(frequency_of_letters(name))