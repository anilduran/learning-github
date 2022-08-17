class Person:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def greet(self):
        print('Hello! My name is ' + self.firstName + ' ' + self.lastName + '.')
