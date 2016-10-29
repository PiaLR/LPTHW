# imports feature argv from module sys
from sys import argv

# defines "script" and "input_file" as variables for argv
script, input_file = argv

# defines a function called "print_all" with an argument / variable "f"
# function will read and print content of f given
def print_all(f):
    print f.read()

# defines a function called "print_all" with an argument / variable "f"
# function will set given f's current position at the offset
def rewind(f):
    f.seek(0)

# defines a function called "print_all" with two arguments / variables "line_count" and "f"
# function will print given value for line_count and read & print one line of the content of f given
def print_a_line(line_count, f):
    print line_count, f.readline()

# defines value for variable "current_file" as opening the file given as input_file by user
current_file = open(input_file)

# prints text
print "First let's print the whole file:\n"

# runs "print_all" function
# reads and prints content of file given by user in the beginning
print_all(current_file)

# prints text
print "Now let's rewind, kind of like a tape."

# runs "rewind" function
# set current position of file given by user in the beginning at the offset (no return value)
rewind(current_file)

# prints text
print "Let's print three lines:"

# assigns value "1" to variable "current_line"
current_line = 1
# runs "print_a_line" function
# prints given value for line_count (= current_line = 1); reads & prints first line of the content of f given (because seek was used before)
print_a_line(current_line, current_file)

# adds "1" to value of variable "current_line"; new value = 2
current_line += 1
# runs "print_a_line" function
# prints given value for line_count (= current_line = 2); reads & prints next (2nd) line of the content of f given
print_a_line(current_line, current_file)

# adds "1" to value of variable "current_line"; new value = 3
current_line += 1
# runs "print_a_line" function
# prints given value for line_count (= current_line = 3); reads & prints next (3rd) line of the content of f given
print_a_line(current_line, current_file)
