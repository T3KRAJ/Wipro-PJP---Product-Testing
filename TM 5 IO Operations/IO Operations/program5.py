# Tek Raj Joshi
# Superset ID: 1368453

with open('filename.txt', mode='r', encoding = 'utf-8') as f:
    words= f.read().split()
    maxl = len(max(words, key=len))
    print( "largest word is:", [word for word in words if len(word) == maxl])