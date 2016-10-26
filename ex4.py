# Defines a value (=100) for the variable "cars".
cars = 100
# Defines a value (=4.0) for the variable "space_in_a_car".
space_in_a_car = 4.0 # floating point number doesn't seem to be necessary in this case?!
# Defines a value (=30) for the variable "drivers".
drivers = 30
# Defines a value (=90) for the variable "passengers".
passengers = 90
# Defines a value (=70) for the variable "cars_not_driven" by referring to the values of the variables "cars" (=100) and "drivers" (=30).
cars_not_driven = cars - drivers
# Defines a value (=30) for the variable "cars_driven" by referring to the value of the variable "drivers" (=30).
cars_driven = drivers
# Defines a value (=120.0) for the variable "carpool_capacity" by referring to and multiplying the values of the variables "cars_driven" (=30) and "space_in_a_car" (=4.0).
carpool_capacity = cars_driven * space_in_a_car
# Defines a value (=3) for the variable "average_passengers_per_car" by referring to the values of the variables "passengers" (=90) and "cars_driven" (=30) and dividing the first by the latter.
average_passengers_per_car = passengers / cars_driven

# Searches for variable "cars" and prints the value it was defined with (=100).
print "There are", cars, "cars available."

# Searches for variable "drivers" and prints the value it was defined with (=30).
print "There are only", drivers, "drivers available."

# Searches for variable "cars_not_driven" and prints the value it was defined with (=100-30=70).
print "There will be", cars_not_driven, "empty cars today."

# Searches for variable "carpool_capacity" and prints the value it was defined with (=30*4.0=120.0).
print "We can transport", carpool_capacity, "people today."

# Searches for variable "passengers" and prints the value it was defined with (=90).
print "We have", passengers, "to carpool today."

# Searches for variable "average_passengers_per_car" and prints the value it was defined with (=90/30=3).
print "We need to put about", average_passengers_per_car, "in each car."

# Zed's mistake explained:
# He defined "carpool_capacity" but later used the term "car_pool_capacity" to refer to it.
# Python can't recognize the variable unless every single character is exactly the same.
# The additional underscore between "car" and "pool" caused that error.
