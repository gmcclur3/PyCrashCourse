# Gary McClure 2016-02-08

pizzas = ['sausage', 'meatball', 'pepperoni', 'sweet peppers and onions']
for pizza in pizzas:
    print("I like " + pizza.title() + " Pizza.")

print("\nI really Like Pizza!")

print("The first three items in the list are:")
print(pizzas[:3])

print("Three items from the middle of the list are:")
print(pizzas[1:3])

print("The last three items in the list are:")
print(pizzas[-3:])

friends_pizza = pizzas[:]
pizzas.append('hawaiian')
friends_pizza.append('bacon')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizza:
    print(pizza)

