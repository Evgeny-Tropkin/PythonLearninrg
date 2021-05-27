class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id
        self.student_id = self.name[0] + self.last_name + str(self.birth_year)

    def print_id(self):
        print(self.student_id)


entered_name = input()
entered_last_name = input()
entered_birth_year = int(input())

student = Student(entered_name, entered_last_name, entered_birth_year)
student.print_id()
