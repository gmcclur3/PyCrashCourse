# Gary McClure 2016-02-10

# 5 True statements
car = 'audi'
print("Is car == to audi? I predict yes")
print(car == 'audi')

pizza = 'cheese'
print("Did you order a cheese pizza? I predict yes!")
print(pizza == 'cheese')

baby = 'male'
print("So you are having a baby! Bet it's a boy")
print(baby == 'male')

cheese = 'cheddar'
print("I bet you order cheddar on your burger!")
print(cheese == 'cheddar')

face = 'punch'
print("I bet you prefer a punch in the face over a kick!")
print(face == 'punch')

# 5 False statements

car = 'Jeep'
print("Is car == to audi? I predict not this time!")
print(car == 'audi')

pizza = 'cheese'
print("Did you order a cheese pizza? I say NO!")
print(pizza == 'peppers')

baby = 'male'
print("So you are having a baby! Bet it's not a boy")
print(baby == 'female')

cheese = 'cheddar'
print("I bet you did not order cheddar on your burger!")
print(cheese == 'swiss')

face = 'punch'
print("I bet you prefer a punch in the face over a kick!")
print(face == 'kick')

# Test Using lower()

name = 'Gary'
print("Case Matters! Gary != gary")
print(name == 'Gary')

name = 'Gary'
print("So if I lower it, it no longer works!")
print(name.lower() == 'Gary')

# Numerical tests

age = 42
print("I bet you are 42")
print(age == 42)
print("Are you 43?")
print(age == 43)
print("I bet you are between 40 and 45")
print(40 < age < 46)
print(age <= 40 or age == 42)

# Test item is/not in a list

favorite_books = ['It', 'The Road']
unfavorite_book = 'Beaches'
best_book = 'It'

if unfavorite_book not in favorite_books:
    print(favorite_books)

if best_book in favorite_books:
    print(favorite_books)






