name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.00*2.54 # inches to cm
weight = 180.00*0.45 # lbs to kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r cm tall." % height
print "He's %i kg heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %f, %F, and %f I get %F." % (age, height, weight, age + height + weight)
