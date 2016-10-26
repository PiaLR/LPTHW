from sys import argv

script, first = argv

print "The script is called:", script
print "Your variable is:", first

understanding = raw_input("Do you understand this? ")
print "%r, you do(n't)! :)" % understanding 
