from admin import Admin
from student import Student
from teacher import Teacher
# Prompt the user to enter details for a student, a teacher, and an admin.
# 6. Create objects of the Student, Teacher, and Admin classes with the provided details.
# Display the information of all three objects using their respective display methods.

class Main:

    print("Enter Student Details:")
    student_name = input("Name: ")
    student_age = int(input("Age: "))
    student_gender = input("Gender: ")
    student_roll_number = input("Roll Number: ")
    student_class = input("Class: ")

    print("\nEnter Teacher Details:")
    teacher_name = input("Name: ")
    teacher_age = int(input("Age: "))
    teacher_gender = input("Gender: ")
    teacher_subject = input("Subject: ")
    teacher_experience = int(input("Experience (in years): "))

    print("\nEnter Admin Details:")
    admin_name = input("Name: ")
    admin_age = int(input("Age: "))
    admin_gender = input("Gender: ")
    admin_roll_number = input("Roll Number: ")
    admin_class = input("Class: ")
    admin_subject = input("Subject: ")
    admin_experience = int(input("Experience (in years): "))
    admin_salary = float(input("Salary: "))
    admin_position = input("Position: ")

    # Create objects

    student = Student()
    teacher = Teacher(teacher_name, teacher_age, teacher_gender, teacher_subject, teacher_experience)
    admin = Admin(admin_name, admin_age, admin_gender, admin_roll_number, admin_class, admin_subject, admin_experience, admin_salary, admin_position)

    # Display information
    print("\nStudent Information:")
    student.display_student_info()

    print("\nTeacher Information:")
    teacher.display_teacher_info()

    print("\nAdmin Information:")
    admin.display_admin_info()