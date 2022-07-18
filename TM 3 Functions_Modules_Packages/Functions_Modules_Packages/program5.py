# Tek Raj Joshi
# Superset ID: 1368453

def get_even(nums):
    even_nums = []
    for i in nums:
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums

array_of_integers = list(map(int, input("Enter the space seperated integers: ").split()))
print(get_even(array_of_integers))