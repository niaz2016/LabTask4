#Define the Admin class, which inherits from both the Student and Teacher
#classes. The Admin class should have additional attributes for salary and
#position, as well as methods for displaying admin-specific information
from student import Student
from teacher import Teacher


class Admin(Student, Teacher):
    def __init__(self, name, age, gender, experience, salary, position, stClass, rollNum, subject):
        Student(name, age, gender, stClass, rollNum)
        Teacher(name, age, gender, subject, experience)
        self.experience = experience
        self.salary = salary
        self.position = position

    def display_admin_info(self):
        self.display_info()
        print(f"Experience: {self.experience} years")
        print(f"Salary: ${self.salary}")
        print(f"Position: {self.position}")
