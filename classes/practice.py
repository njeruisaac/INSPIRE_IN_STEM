#1/usr/bin/python
class employee:
    def __init__(self, _name, _salary, _id):
        self.name= _name
        self.salary=_salary
        self.id=_id

    def sayHi(self):
        print("Hello my name is " + self.name, "My Id number is "+ self.id, "My salary is "+self.salary)
employee1= employee("James", str(3500400),str(39277231) )
employee1.sayHi()