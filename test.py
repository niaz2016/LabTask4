class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, stClass, rollNum):
        Person.__init__(self, name, age, gender)  # Call Person constructor explicitly
        self.stClass = stClass
        self.rollNum = rollNum

    def display_student_info(self):
        self.display_info()
        print(f"Roll Number: {self.rollNum}")
        print(f"Class: {self.stClass}")


class Teacher(Person):
    def __init__(self, name, age, gender, subject, salary):
        Person.__init__(self, name, age, gender)  # Call Person constructor explicitly
        self.subject = subject
        self.salary = salary

    def display_teacher_info(self):
        self.display_info()
        print(f"Subject: {self.subject}")
        print(f"Salary: {self.salary}")


class Admin(Student, Teacher):
    def __init__(self, name, age, gender, stClass, rollNum, subject, salary, role):
        # Explicitly call constructors to avoid super() MRO conflicts
        Student.__init__(self, name, age, gender, stClass, rollNum)
        Teacher.__init__(self, name, age, gender, subject, salary)
        self.role = role

    def display_admin_info(self):
        print("Admin Details:")
        self.display_info()  # Display shared attributes
        print(f"Roll Number: {self.rollNum}")  # Student-specific
        print(f"Class: {self.stClass}")  # Student-specific
        print(f"Subject: {self.subject}")  # Teacher-specific
        print(f"Salary: {self.salary}")  # Teacher-specific
        print(f"Role: {self.role}")  # Admin-specific


# Example Usage
print("Enter Admin Details:")
admin_name = input("Name: ")
admin_age = int(input("Age: "))
admin_gender = input("Gender: ")
admin_class = input("Class (if a Student): ")
admin_roll = input("Roll Number (if a Student): ")
admin_subject = input("Subject (if a Teacher): ")
admin_salary = float(input("Salary (if a Teacher): "))
admin_role = input("Role (Admin): ")

# Create Admin object
admin = Admin(admin_name, admin_age, admin_gender, admin_class, admin_roll, admin_subject, admin_salary, admin_role)

# Display Admin details
admin.display_admin_info()
