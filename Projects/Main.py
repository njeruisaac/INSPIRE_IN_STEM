#1/usr/bin/python
import Operations
from teachers import Teachers
import student

print(Operations.diff_numbers(3,5))
print(Operations.sub_numbers(80,4))
print(Operations.mult_numbers(40,5))
print(Operations.add_numbers(4,15))

# new_student = Student("Joan", "Cycling", "1990")
# Student.greet_student()
# print(Student)

new_teacher = Teachers("James",45090,"CRE","Ksh.30000") 
print(new_teacher.get_name())