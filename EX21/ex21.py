def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide (100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
print "Yes, I can: ", (30 + 5) + ((78 - 4) - ((90 * 2) * ((100 / 2) / 2)))

print "Here's the result of my simple formula: ", 4 * 5 + 3 - 2 / 10 + 100 - 400 * (7 - 8)
print "And here's the result calculated with the functions: ", add(subtract(add(multiply(4, 5), 3), divide(2, 10)), multiply(400, subtract(7, 8)))

print 24 + 34 / 100 - 1023
sth = add(24, subtract(divide(34, 100), 1023))
print sth
