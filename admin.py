#Define the Admin class, which inherits from both the Student and Teacher
#classes. The Admin class should have additional attributes for salary and
#position, as well as methods for displaying admin-specific information
from student import Student
from teacher import Teacher


class Admin(Student, Teacher):
    def _init_(self, name, age, gender, roll_number, student_class, subject, experience, salary, position):
        Student._init_(self, name, age, gender, roll_number, student_class)
        Teacher._init_(self, name, age, gender, subject, experience)
        self.salary = salary
        self.position = position

    def display_admin_info(self):
        self.display_info()
        print(f"Roll Number: {self.roll_number}")
        print(f"Class: {self.student_class}")
        print(f"Subject: {self.subject}")
        print(f"Experience: {self.experience} years")
        print(f"Salary: ${self.salary}")
        print(f"Position: {self.position}")
