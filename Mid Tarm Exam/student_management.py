class StudentDatabase:
    
    student_list = []
    @classmethod
    def add_student(cls,student_info):
        cls.student_list.append(student_info)

    @classmethod
    def find_st_id(cls,st_id):
        for st in cls.student_list:
            if st.get_id() == st_id:
                return st
        return None
    
    @classmethod
    def view_all(cls):
        print("\n------------------------------------------")
        for st in cls.student_list:
            st.view_student_info()
        print("-----------------------------------------")




class Student:
    def __init__(self,student_id,name,department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False

    def get_id(self):
        return self.__student_id


    def enroll_student(self):
        if self.__is_enrolled:
            print(f"\nID: {self.__student_id} Already enrolled")
        else:
            self.__is_enrolled = True
            print(f'\nID: {self.__student_id} has been enrolled')

        

    
    def drop_student(self):
        if not self.__is_enrolled:
            print(f"\nID: {self.__student_id} Not enrolled")
        else:
            self.__is_enrolled = False
            print(f'\nID: {self.__student_id} has been dropped')
        

    
    def view_student_info(self):
            print(f'\nID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}')
        

s1 = Student('s333','Jakaria','Science')
s3 = Student('s444','Tandra','Physics')
s2 = Student('s555','Emon','Mathematics')

StudentDatabase.add_student(s1)
StudentDatabase.add_student(s2)
StudentDatabase.add_student(s3)

print(StudentDatabase.find_st_id('s333'))


while True:
    print("\n--- student Management Menu ---")
    print("1. View all Student")
    print("2. Enroll Student")
    print("3. Drop student")
    print("4. Exit")
    option = int(input("\nEnter your choice (1-4): "))

    if option == 1:
        StudentDatabase.view_all()
    elif option == 3:
        id = input("Enter student ID to drop: ")
        st = StudentDatabase.find_st_id(id)
        if st:
            st.drop_student()
        else:
            print("Invalid student ID")
    elif option == 2:
        id = input("Enter student ID to Enroll: ")
        st = StudentDatabase.find_st_id(id)
        if st:
            st.enroll_student()
        else:
            print("Invalid student ID")
    elif option == 4:
        break
    else:
        print("\n------- please choice the right option ----------")