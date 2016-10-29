print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formular(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# runs "secret_formular" with "10000" (=start_point) as value for started
beans, jars, crates = secret_formular(start_point)

print "With a starting point of: %d" % start_point
# "beans" and "jelly_beans" are both just variables; return will give number as value
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# value for start_point becomes "1000" ...
start_point = start_point / 10

print "We can also do that this way:"
# ... therefore values are /10 lower this time; otherwise the result would be the same as before
print "We'd have %d beans, %d jars, and %d crates." % secret_formular(start_point)
