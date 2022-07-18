# Tek Raj Joshi
# Superset ID: 1368453

no_of_lines_to_display = int(input("Enter the number of lines you want to display: "))
with open('filename.txt', mode='r', encoding = 'utf-8') as f:
    for line in range(no_of_lines_to_display):
        print(f.readline())
    f.close()