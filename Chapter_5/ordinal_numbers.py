# Gary McClure 2016-02-15

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if ordinal_numbers:
    for ordinal_number in ordinal_numbers:
        if ordinal_number == 1:
            print("1st")
        elif ordinal_number == 2:
            print("2nd")
        elif ordinal_number == 3:
            print("3rd")
        else:
            print(str(ordinal_number) + "th")
else:
    print("Your empty list is empty!")
