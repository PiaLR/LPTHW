## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
    def cute(self):
        print "Any animal is cute."

## class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has-a __init__ that takes self and name parameters
        self.name = name

    def bark(self, name):
        print "%s barks loud." % name

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has-a __init__ that takes self and name parameters
        self.name = name

    def meow(self, name):
        print "%s meows quietly." % name

## class Person is-a object
class Person(object):

    def __init__(self, name):
        ## class Person has-a __init__ that takes self and name parameters
        self.name = name

        ## Person has- a pet of some kind
        self.pet = None

    def cuddle(self, name):
        print "%s cuddles pet." % name

## class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## from superclass Person get the __init__ function and call it with parameters Employee, self, name
        super(Employee, self).__init__(name)
        ## from self get salary attribute and set it to salary
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## stan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee with salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

Pia = Person("Pia")
Pia.cuddle("Pia")

Danny = Dog("Danny")
Danny.bark("Danny")

Mogli = Cat("Mogli")
Mogli.meow("Mogli")
Mogli.cute()
