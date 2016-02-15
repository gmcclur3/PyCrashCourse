# Gary McClure 2016-02-15

users = ['admin', 'gm', 'loki', 'cap', 'dad']

if users:
    for user in users:
        if user == 'admin':
            print("Hello Boss!")
        else:
            print("Thank you for logging in " + user + "!")
else:
    print("We need to get some users!")
