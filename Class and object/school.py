class Student:

    def __init__(self,name,current_class,roll):
        self.name = name
        self.current_class = current_class
        self.roll = roll
    
    def __repr__(self):
        return f'student name : {self.name} class : {self.current_class} roll : {self.roll}'

class Teacher:

    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self):
        return f'teacher name : {self.name} subject : {self.subject} teacher_id : {self.id}'


class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teacher(self , name,subject):
        id = len(self.teachers)+101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)
    
    def add_student(self,name,fee):
        id = len(self.students)+1
        st = Student(name,'c',id)
        self.students.append(st)


j = Student("jakaria","six",4)

print(j)

s = Teacher("sumon","englis",4323)

print(s)