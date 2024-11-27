#Define the Teacher class, which also inherits from the Person class. The Teacher
#class should have additional attributes for subject and experience, as well as
#methods for displaying teacher-specific information.

from person import Person

class Teacher(Person):
    def _init_(self, name, age, gender, subject, experience):
        super()._init_(name, age, gender)
        self.subject = subject
        self.experience = experience

    def display_teacher_info(self):
        self.display_info()
        print(f"Subject: {self.subject}")
        print(f"Experience: {self.experience} years")

