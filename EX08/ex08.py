# assigns string on the right as value to variable "formatter"; this string includes formatter %r four times
formatter = "%r %r %r %r"

# prints value assigned to variable "formatter" including values defined for formatters %r; defines "1" "2" "3" "4" as values for the four "%r"s
print formatter % (1,2,3,4)
# prints value assigned to variable "formatter" including values defined for formatters %r; defines "one" "two" "three" "four" as values for the four "%r"s
print formatter % ("one", "two", "three", "four")
# prints value assigned to variable "formatter" including values defined for formatters %r; defines "True" "False" "False" "True" as values for the four "%r"s
print formatter % (True, False, False, True)
# prints value assigned to variable "formatter" including values defined for formatters %r; defines variable "formatter" as value for the four "%r"s; therefore prints "%r %r %r %r" four times in a row
print formatter % (formatter, formatter, formatter, formatter)
# same procedure as before; this time the first %r is defined as string/ text "I had this thing." and so on
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
