# Tek Raj Joshi
# Superset ID: 1368453

list_of_tuples = [(10,20,40), (40,50,60), (70,80,90)]
new_item = int(input("New item to be added: "))
updated_last_tuple = list(list_of_tuples[-1])
updated_last_tuple[-1] = new_item
list_of_tuples[-1] = updated_last_tuple
print(list_of_tuples)