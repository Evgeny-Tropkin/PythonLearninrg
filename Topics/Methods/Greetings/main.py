class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, I am " + self.name + "!"


entered_name = input()

new_person = Person(entered_name)
print(new_person.greet())
