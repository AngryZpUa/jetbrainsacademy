class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return "Hello, I am {0}!".format(self.name)


person_name = input()
person = Person(person_name)
print(person.greet())
