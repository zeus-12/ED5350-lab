name = "vishnu"
rollno="73"

physics = 40
maths= 40
chemistry = 30

course_list = ["math","phyics","biology"]
cgpa = 9

class Student:
    def get_details(self,name,rollno):
        self.student_name = name
        self.roll_number = rollno

    def print_details(self):
        print(f"Name:{self.student_name}, Roll Number:{self.roll_number}")

student1 = Student()

student1.get_details(name, rollno)
student1.print_details()

class JEE(Student):
    def get_marks(self, physics_marks,chemistry_marks,maths_marks):
        self.physics_marks = physics_marks
        self.chemistry_marks=chemistry_marks
        self.maths_marks = maths_marks
    
    def print_details(self):
        print(f"Physics Marks:{self.physics_marks}, Chemistry Marks:{self.chemistry_marks}, Maths Marks:{self.maths_marks}")
        print(f"Name:{self.student_name}, Roll Number:{self.roll_number}")


jee_student1 = JEE()
jee_student2 = JEE()

jee_student1.get_details(name, rollno)
jee_student2.get_details("thazeel", "69")


jee_student1.get_marks(physics, chemistry,maths)
jee_student2.get_marks(50, 50,50)

jee_student1.print_details()
jee_student2.print_details()

class Semester(JEE):
    def get_sem_details(self,courses,cgpa):
        self.courses=courses
        self.cgpa = cgpa
    
    def print_details(self):
        print(f"Courses:{self.courses}, Cgpa:{self.cgpa}")
        print(f"Physics Marks:{self.physics_marks}, Chemistry Marks:{self.chemistry_marks}, Maths Marks:{self.maths_marks}")
        print(f"Name:{self.student_name}, Roll Number:{self.roll_number}")
    
smstr1 = Semester()
smstr2= Semester()

smstr1.get_details(name,rollno)
smstr2.get_details("thazeel", "69")

smstr1.get_marks(physics, chemistry,maths)
smstr2.get_marks(50, 50,50)

smstr1.get_sem_details(course_list,cgpa)
smstr2.get_sem_details(["physics","maths"], 9.5)

smstr1.print_details()
smstr2.print_details()