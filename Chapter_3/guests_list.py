#Gary McClure 2016-02-07

guests = ['kurt vonnegut', 'otis redding', 'stephen king']

print("Dear " + guests[0].title() + " please come to dinner on Tuesday")
print("Dear " + guests[1].title() + " please come to dinner on Tuesday")
print("Dear " + guests[2].title() + " please come to dinner on Tuesday")


# Someone can't make the party

popped_guest = guests.pop()

print("Oh no, " + popped_guest.title() + " can no longer make it to dinner!")

guests.append('thomas jefferson')

print("I guess I will ask " + guests[2] + " instead")


print("Dear " + guests[0].title() + " please come to dinner on Tuesday")
print("Dear " + guests[1].title() + " please come to dinner on Tuesday")
print("Dear " + guests[2].title() + " please come to dinner on Tuesday")

# Just found a larger venue

print("Awesome I just found a larger venue! I can invite three more people!")

guests.insert(0, 'edward abbey')
guests.insert(2, 'groucho marx')
guests.append('steve martin')

print("Dear " + guests[0].title() + " please come to dinner on Tuesday")
print("Dear " + guests[1].title() + " please come to dinner on Tuesday")
print("Dear " + guests[2].title() + " please come to dinner on Tuesday")
print("Dear " + guests[3].title() + " please come to dinner on Tuesday")
print("Dear " + guests[4].title() + " please come to dinner on Tuesday")
print("Dear " + guests[5].title() + " please come to dinner on Tuesday")

# Venue lost the larger table. Now only room for two guests

print("Oh no, the venue lost their larger table. I need to shrink the list to just two people!")

popped_guest = guests.pop()

print("Sorry " + popped_guest.title() + " I ran out of space! No dinner for you!")

popped_guest = guests.pop()

print("Sorry " + popped_guest.title() + " I ran out of space! No dinner for you!")

popped_guest = guests.pop()

print("Sorry " + popped_guest.title() + " I ran out of space! No dinner for you!")

popped_guest = guests.pop()

print("Sorry " + popped_guest.title() + " I ran out of space! No dinner for you!")

print(guests[0].title() + " you are still invited to dinner!")
print(guests[1].title() + " you are still invited to dinner!")
guests_len = len(guests)
print("Final number of guests is: " + str(guests_len) + ".")

del guests[0]
del guests[0]

print(guests)

