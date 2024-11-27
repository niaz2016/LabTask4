#Define the Person class with attributes for name, age, and gender. This class
#should also have methods for displaying basic information about a person
class Person:
    def _init_(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
