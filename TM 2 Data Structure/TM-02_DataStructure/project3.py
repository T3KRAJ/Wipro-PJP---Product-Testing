# Tek Raj Joshi
# Superset ID: 1368453

students_records = {
    "Krishna": [67,68,69],
    "Arjun": [70,98,63],
    "Malika": [52,56,60]
}

student_name = input("Enter Student Name: ")
print(sum(students_records[student_name])/len(students_records[student_name]))