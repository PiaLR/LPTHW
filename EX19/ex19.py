# defines a function named "cheese_and_crackers" with the two arguments /variables "cheese_count" and "boxes_of_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints text including value given for cheese_count which then replaces formatter
    print "You have %d cheeses!" % cheese_count
    # prints text including value given for boxes_of_crackers which then replaces formatter
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # prints text
    print "Man that's enough for a party!"
    # prints text using escape
    print "Get a blanket.\n"

# prints text and then all the text of the "cheese_and_crackers"-function; 20 becomes value for cheese_count; 30 becomes value for boxes_of_crackers
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# prints text
print "OR, we can use variables from our script:"
# defines value 10 for variable "amount_of_cheese"
amount_of_cheese = 10
# defines value 50 for variable "amount_of_crackers"
amount_of_crackers = 50

# prints all the text of the "cheese_and_crackers"-function; amount_of_cheese (=10) becomes value for cheese_count; amount_of_crackers (=50) becomes value for boxes_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints text
print "We can even do math inside too:"
# prints all the text of the "cheese_and_crackers"-function; calculates additions; the first result (=30) becomes value for cheese_count; the second result (=11) becomes value for boxes_of_crackers
cheese_and_crackers(10 + 20, 5 + 6)

# prints text
print "And we can combine the two, variables and math:"
# prints all the text of the "cheese_and_crackers"-function
# variable amount_of_cheese in addition to 100 becomes value for cheese_count; variable amount_of_crackers in addition to 1000 becomes value for boxes_of_crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
