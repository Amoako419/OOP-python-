class Student:
    def __init__(self,name,roll_num,marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks

student1  = Student('Kofi',1234,90)

print(student1.name)