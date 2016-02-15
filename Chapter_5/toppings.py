# Gary McClure 2016-02-08

requested_toppings = ['mushrooms', 'extra cheese']

if requested_toppings != 'anchovies':
    print("Hold the Anchovies!")
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!\n")

requested_toppings = ['mushrooms', 'extra cheese', 'sausage']

for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print("Sorry, we are out of mushrooms right now")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!\n")

requested_toppings = ['']

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!\n")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'extra cheese', 'sausage']
requested_toppings = ['mushrooms', 'extra cheese', 'sausage', 'dog']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished Making your pizza!\n")
