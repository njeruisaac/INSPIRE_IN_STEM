# !/usr/bin/python
#####################################################
#       Name : Isaac NJERU
#       Date : 2 / 6 / 22.
#####################################################

#create name and the employee salary

class employee:
    def __init__(self,name,salary,job):
        self.name=name
        self.salary=salary
        self.job=job

    def sayHi(self):
        print("My name is ",self.name, "I earn ",self.salary, "I work as a ",self.job,)

employee1=employee("John", str(54000),"Accountant")
employee1.sayHi()
employee2=employee("Rose", str(30000),"Secretary")
employee2.sayHi()
employee3=employee("Sam",str(550000),"CFO")
employee3.sayHi()