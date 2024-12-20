# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.grade=0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.grade=5
    student2.name = "Olivia"
    student2.age = 21
    student2.grade=3.5
    student3.name = "Max"
    student3.age = 20
    student3.grade=3.9
    

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, grade = {student1.grade}')
    print(f'{student2.name}, {student2.age} years old, grade = {student2.grade}')
    print(f'{student3.name}, {student3.age} years old, grade = {student3.grade}')
    print(Student())

if __name__ == "__main__":
    main()