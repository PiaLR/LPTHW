class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

# will print "PARENT implicit()" --> no override
dad.implicit()
# will print "PARENT implicit()" --> no override
son.implicit()

# will print "PARENT override()" --> no override
dad.override()
# will print "CHILD override()" --> override
son.override()

# will print "PARENT altered()" --> no override
dad.altered()
# will print "CHILD, BEFORE PARENT altered()" --> override
# will print "PARENT altered()" --> no override
# will print "CHILD, AFTER PARENT altered()" --> override 
son.altered()
