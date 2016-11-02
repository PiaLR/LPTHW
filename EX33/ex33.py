i = 0
k = 9
h = 2
numbers = []

def numbers_function (i, k):
    while i < k:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + h
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

numbers_function (i, k)

print "The numbers: "

for num in numbers:
    print num

numbers_function (4, 15)

print "The numbers: "

for num in numbers:
    print num
