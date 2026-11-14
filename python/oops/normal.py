# class Student:
#     name = "satyam sharma"

# s1 = Student()
 

class Student:
    college = "acfd college"

    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("Adding new students in")
    
    @staticmethod  
    def hello():
        print("hello")

    def welcome(self):
        print("Welcome students,",self.name)


s1 = Student("satyam",33)
print(s1.name, s1.marks, s1.college)

s2 = Student("sharma",222)
print(s2.name, s2.marks) 
 
s1.welcome()
s1.hello()