# Gary McClure 2016-02-08

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)


# cleaner

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)


# list comprehensions

squares = [value**2 for value in range(1,11)]
print(squares)

