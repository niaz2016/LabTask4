from admin import Admin
from person import Person
from student import Student
from teacher import Teacher
# Prompt the user to enter details for a student, a teacher, and an admin.
# 6. Create objects of the Student, Teacher, and Admin classes with the provided details.
# Display the information of all three objects using their respective display methods.

class Main:

    
    def getInput(title,type="text"):
        title=title+': '
        if (type=="text"):
            return input(title)
        elif (type=="number"):
            return int(input(title))
        elif (type=="float"):
            return float(input(title))

    # Create objects
    print("Enter Student Details:")
    student = Student(getInput("Name"), getInput("Age","number"), getInput("Gender"), getInput("Class"), getInput("Roll No","number"))
    print("\nEnter Teacher Details:")
    teacher = Teacher(getInput("Name"), getInput("Age","number"), getInput("Gender"), getInput("Subject"), getInput("Experience","number"))
    print("\nEnter Admin Details:")
    admin = Admin(getInput("Name"), getInput("Age","number"), getInput("Gender"), getInput("Experiance","number"), getInput("Sallary","number"), getInput("Position"),  getInput("Class"), getInput("Roll No","number"), getInput("Subject"))
    
    # Display information
    print("\nStudent Information:")
    student.display_student_info()

    print("\nTeacher Information:")
    teacher.display_teacher_info()

    print("\nAdmin Information:")
    admin.display_admin_info()