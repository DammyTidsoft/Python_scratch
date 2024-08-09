'''
We can create our own data type in python
and you can create a class
for example check student.py
the first line of code is calling the student file and the student class at a time  
'''
from Student import Student
student1 = Student("Jim", "Business", 3.1, 25, "Male", False)
print(student1.name)
print(student1.age)
print(student1.gpa)
student2 = Student("Bunmi","Marketer", 4.5, 28, "Female", True)
print(student2.is_on_probation)