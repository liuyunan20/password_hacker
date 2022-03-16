import itertools


# first_names = ['Anna', 'Catarina']
# middle_names = ['Luisa', 'Maria']
for element in itertools.product(first_names, middle_names):
    print(*element, sep=" ")
