# assigns string on the right as value to variable "x"; formatter %d stands for value entered behind % (=10)
x = "There are %d types of people." % 10
# assigns string "binary" as value to variable "binary"
binary = "binary"
# assigns string "don't" as value to variable "do_not"
do_not = "don't"
# assigns string on the right as value to variable "y"; formatters %s stand for values entered behind %
y = "Those who know %s and those who %s." % (binary, do_not) # [strings in string]

# prints value defined for x including value defined for %d
print x
# prints value defined for y including values defined for %s (in the order they were written before)
print y

# formatter %r stands for variable x; prints string including value defined for x including value defined for %d
print "I said: %r." % x # [string in string]
# formatter %s stands for variable y; prints string including value defined for y including values defined for %s
print "I also said: '%s'." % y # [string in string]

# assigns value "False" to variable "hilarious"
hilarious = False
# assigns string on the right as value to variable "joke_evaluation"; includes formatter %r
joke_evaluation = "Isn't that joke so funny?! %r"

# prints value defined for "joke_evaluation" including value defined for %r; defines variable "hilarious" as value for "%r"
print joke_evaluation % hilarious

# assigns string on the right as value to variable "w"
w = "This is the left side of..."
# assigns string on the right as value to variable "e"
e = "a string with a right side."

# prints values defined for "w" and "e" after one another
print w + e
