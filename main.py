from admin import Admin
from person import Person
from student import Student
from teacher import Teacher
# Prompt the user to enter details for a student, a teacher, and an admin.
# 6. Create objects of the Student, Teacher, and Admin classes with the provided details.
# Display the information of all three objects using their respective display methods.

class Main:

    def name():
        return input("Name: ")
    def age():
        return int(input("Age: "))
    def gender():
        return input("Gender: ")
    def rollNum():
        return input("Roll Number: ")
    def askClass():
        return input("Class: ")
    def subject():
        return input("Subject: ")
    def experience(): 
        return int(input("Experience (in years): "))
    def sallary():
        return float(input("Salary: "))
    def position():
        return input("Position: ")

    # Create objects
    print("Enter Student Details:")
    student = Student(name(), age(), gender(), askClass(), rollNum())
    print("\nEnter Teacher Details:")
    teacher = Teacher(name(), age(), gender(),subject(), experience())
    print("\nEnter Admin Details:")
    admin = Admin(name(), age(), gender(), experience(), sallary(), position(),  askClass(), rollNum(), subject())
    
    # Display information
    print("\nStudent Information:")
    student.display_student_info()

    print("\nTeacher Information:")
    teacher.display_teacher_info()

    print("\nAdmin Information:")
    admin.display_admin_info()