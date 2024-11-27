#Define the Student class, which inherits from the Person class. The Student class
#should have additional attributes for roll number and class, as well as methods
#for displaying student-specific information.
from person import Person


class Student(Person):
    def __init__(self, name, age, gender, stClass, rollNum):
        Person.__init__(self, name, age, gender)
        self.stClass = stClass
        self.rollNum = rollNum

    def display_student_info(self):
        self.display_info()
        print(f"Roll Number: {self.rollNum}")
        print(f"Class: {self.stClass}")
