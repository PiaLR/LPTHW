# imports arguable variable feature from sys package
from sys import argv

# defines script (ex15.py) and filename (e.g. ex15_sample.txt) as arguable variables which need to be given by user
script, filename = argv

# defines the value for variable "txt" as [returning] the file object whichs name was typed before [not visible yet]
txt = open(filename)

# prints the text including the filename which was given earlier by replacing formatter with it
print "Here's your file %r:" % filename
# gives the file 'behind' variable "txt" the read command [with no parameters]; prints that content
print txt.read()

txt.close()
print "Your file %r has now been closed." % filename

# prints the text
print "Type the filename again:"
# defines the value for variable "file_again" as the file object whichs name is now typed by user via raw_input
file_again = raw_input("> ")

# defines the value for variable "txt_again" as [returning] the file object whichs name was typed before via raw_input [not visible yet]
txt_again = open(file_again)

# gives the file 'behind' variable "txt_again" the read command [with no parameters]; prints that content
print txt_again.read()

txt_again.close()
print "Your file %r has now been closed." % file_again

# personally I think the raw_input method is more user-friendly; with argv you need to know what input file ex15.py needs before being able to use it
# on another note, by using argv (and as a user knowing how to handle it in this case) you get to the result (=printed content of file) much faster
