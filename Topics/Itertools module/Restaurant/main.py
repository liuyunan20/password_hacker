import itertools


# main_courses = ['beef stew', 'fried fish']
# price_main_courses = [28, 23]
#
# desserts = ['ice-cream', 'cake']
# price_desserts = [2, 4]
#
# drinks = ['cola', 'wine']
# price_drinks = [3, 10]

dishes = itertools.product(main_courses, desserts, drinks)
prices = itertools.product(price_main_courses, price_desserts, price_drinks)
for dish, price in zip(dishes, prices):
    if sum(price) <= 30:
        print(*dish, sum(price), sep=" ")
