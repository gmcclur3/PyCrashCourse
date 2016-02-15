# Gary McClure 2016-02-15

current_users = ['admin', 'gm', 'loki', 'cap', 'dad']
new_users = ['carl,', 'rick', 'Dad']

if new_users:
    for new_user in new_users:
        if new_user.lower in current_users:
            print("Pick a new name Please!")
        else:
            print("That name is available!")
