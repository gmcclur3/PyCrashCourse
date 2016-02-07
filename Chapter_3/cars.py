# Gary McClure 2016-02-05

cars = ['honda', 'toyota', 'jeep', 'land Rover', 'yugo', 'audi']

message = "A " + cars[0].title() + " is an ok car."
print(message)
message = "A " + cars[1].title() + " is a little better."
print(message)
message = "I would definitely take a " + cars[2].title() + " over the first two."
print(message)
message = "A " + cars[3].title() + " would be even better!"
print(message)
message = "A " + cars[4].title() + " is a disposable car."
print(message)
message = "An " + cars[5].title() + " is a sweet ride!"
print(message)


# Organizing a list

print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Temp sort

cars = ['honda', 'toyota', 'jeep', 'land Rover', 'yugo', 'audi']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again")
print(cars)

# Printing a list in reverse order

print(cars)

cars.reverse()

print(cars)

cars_len = len(cars)

print(cars_len)