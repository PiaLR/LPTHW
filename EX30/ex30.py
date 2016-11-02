# assigns values to variables
people = 30
cars = 40
trucks = 15

# Checks if value for variable "cars" is higher than value for "people"
if cars > people:
    # If so, this line will be printed:
    print "We should take the cars."
# Otherwise checks if value for variable "cars" is lower than value for "people"
elif cars < people:
    # If so, this line will be printed:
    print "We should not take the cars."
# Otherwise, this line will be printed:
else:
    print "We can't decide."

# Checks if value for variable "trucks" is higher than value for "cars"
if trucks > cars:
    # If so, this line will be printed:
    print "That's too many trucks."
# Otherwise checks if value for variable "trucks" is lower than value for "cars"
elif trucks < cars:
    # If so, this line will be printed:
    print "Maybe we could take the trucks."
# Otherwise, this line will be printed:
else:
    print "We still can't decide."

# Checks if value for variable "people" is higher than value for "trucks"
if people > trucks:
    # If so, this line will be printed:
    print "Alright, let's just take the trucks."
# Otherwise, this line will be printed:
else:
    print "Fine, let's stay home then."

# Checks if value for "people" is lower than value for "trucks" and value for "cars" is higher than "people"
if people < trucks and cars > people:
    # If so, this line will be printed:
    print "Do you want to watch tv?"
# Otherwise, this line will be printed:
else:
    print "Ok, let's go!"
