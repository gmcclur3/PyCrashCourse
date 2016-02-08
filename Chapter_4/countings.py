# Gary McClure 2016-02-08

numbers = list(range(1, 21))
for number in numbers:
    print(number)

numbers = list(range(1, 1000001))
for number in numbers:
    print(number)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1,21,2))
print(odd_numbers)

threes = list(range(3,31,3))
for three in threes:
    print(three)

cubes = []
for value in range(1,11):
    cubes.append(value**3)

print cubes

cubes = list(value**3 for value in range(1, 11))
for cube in cubes:
    print(cube)

