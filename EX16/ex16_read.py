from sys import argv

script, filename = argv

test = open(filename)

print test.read()

test.close()

filename2 = raw_input("Type filename to open & print again: ")

test2 = open(filename2)

print test2.read()

test2.close()
