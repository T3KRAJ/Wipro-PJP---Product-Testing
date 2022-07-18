# Tek Raj Joshi
# Superset ID: 1368453

with open('filename.txt', mode='r', encoding = 'utf-8') as f:
    words= f.read().split()
    word = input("Enter the word to get it's frequency: ")
    print(words.count(word))