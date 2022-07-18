# Tek Raj Joshi
# Superset ID: 1368453

file_name = input("enter the file_name: ")

def get_time(file):
    count = 0
    while(file.readline()):
        count += 1
    if count <= 12:
        return str(count) + " AM"
    else:
        return str(count-12) + " PM"

def get_place():
    file = open(file_name)
    file_dict = {}
    data = file.read()
    for i in data.split():
        file_dict[i] = file_dict.get(i, 0) + 1
    m = 0
    place = ""
    for key, value in file_dict.items():
        if value > m:
            m = value
            place = key
    return (place + " Street")

try:
    file = open(file_name)
    print("Meeting Time: ", get_time(file))
    print("Meeting Place: ", get_place())
    file.close()
except:
    print("File does not exist.")


