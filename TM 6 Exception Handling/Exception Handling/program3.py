# Tek Raj Joshi
# Superset ID: 1368453

try:
    with open('filename.txt', mode='r', encoding = 'utf-8') as f:
        print(f.read())
        f.close()
except Exception as e:
    print("Oops! ", e, "occured.")
