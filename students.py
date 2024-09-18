# class Student:
#     def __init__(self,name,roll_num,marks):
#         self.name = name
#         self.roll_num = roll_num
#         self.marks = marks

# student1  = Student('Kofi',1234,90)
# student2 = Student('Ama',567,89)
# print(student1.name)
# print(student2.name)
# print(student1.roll_num)
# print(student2.roll_num)


def remove_duplicates(list):
  Seen = set()
  result = []
  for item in list:
    if item not in Seen:
      Seen.add(item)
      result.append(item)
  return result