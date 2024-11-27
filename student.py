#Define the Student class, which inherits from the Person class. The Student class
#should have additional attributes for roll number and class, as well as methods
#for displaying student-specific information.
from person import Person


class Student(Person):
    def _init_(self, roll_number, student_class):
        super()._init_(name, age, gender)
        self.roll_number = roll_number
        self.student_class = student_class

    def display_student_info(self):
        self.display_info()
        print(f"Roll Number: {self.roll_number}")
        print(f"Class: {self.student_class}")
