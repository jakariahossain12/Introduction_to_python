from school import School
from person import Student,Teacher
from subject import Subject
from classroom import Classroom

school = School("Abx","dhaka")

eight = Classroom("eight")
nine = Classroom("nine")
ten = Classroom("ten")


school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student("rahim",eight)
tondra = Student("tondra",nine)
sumon = Student("sumon",ten)
jakaria = Student("jakaria",ten)

school.student_admission(rahim)
school.student_admission(tondra)
school.student_admission(sumon)
school.student_admission(jakaria)

abul = Teacher("abul")
babul = Teacher("babul")
kabul = Teacher("kabul")

bangla = Subject("Bangla",abul)
physics = Subject("physics",babul)
chemisty = Subject("chemistry",kabul)
biology = Subject("biology",kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemisty)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemisty)
ten.add_subject(chemisty)
ten.add_subject(biology)
ten.add_subject(physics)
ten.add_subject(bangla)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)