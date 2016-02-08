# Gary McClure 2016-02-08

my_foods = ['pizza', 'ice cream', 'pb cups']

friend_foods = my_foods[:]
my_foods.append('ham')
friend_foods.append('cheese')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)



