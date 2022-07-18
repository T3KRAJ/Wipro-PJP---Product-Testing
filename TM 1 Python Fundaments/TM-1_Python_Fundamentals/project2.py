# Tek Raj Joshi
# Superset ID: 1368453

charge_per_hour = 0.51

# cost to operate one server per day
print(24*charge_per_hour)

# cost to operate one server per week
print(7*24*charge_per_hour)

# cost to operate one server per month
print(30*24*charge_per_hour)

# Days we can operate one server with  $918 
total_hours_operating = 918/charge_per_hour
print(int(total_hours_operating/24))