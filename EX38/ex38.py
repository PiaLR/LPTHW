ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    # pop(more_stuff)
    # Call pop on more_stuff; Call pop with argument more_stuff
    print "Adding: ", next_one
    stuff.append(next_one)
    # append(stuff, next_one)
    # Call append on stuff and next_one; Call append with arguments stuff and next_one
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
    # pop(stuff)
    # Call pop on stuff; Call pop with argument stuff
print ' '.join(stuff) # what? cool!
    # join(' ', stuff)
    # Call join on ' ' and stuff; Call join with arguments ' ' and stuff
print '#'.join(stuff[3:5]) # super stellar!
    # join('#', stuff[3:5])
    # Call join on '#' and stuff[3:5]; Call join with arguments '#' and stuff[3:5]
