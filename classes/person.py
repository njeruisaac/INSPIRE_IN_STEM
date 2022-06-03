# !/usr/bin/python
#####################################################
#       Name : Isaac NJERU
#       Date : 2 / 6 / 22.
####################################################

class person:
    def __init__(self,_name,_age,_gender) :
        self.name=_name
        self.age=_age
        self.gender=_gender

    def sayHi(self):
        print("Hi my name is"+ self.name, "I am " +self.age ,"yrs", "I am " + self.gender, )

person1= person("Phillip", str(25), "Male")
person1.sayHi()

person2= person("James", str(19), "Male")
person2.sayHi()

person3=person("Catherin", str(43), "Female")
person3.sayHi()