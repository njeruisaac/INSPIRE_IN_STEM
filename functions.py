#1/usr/bin/python

############################################
#       Name : Isaac Njeru
#       Date : 31 / 5 / 20.
#############################################

#Functions- blocks of code

#defining a function/ initialising
# def say_hello():
#     print("Hello from JKUAT")

# say_hello()

# def bark():
#     print("Dogs bark Woof Woof")
# bark()

# def moo():
#     print("Cows Moo")
# moo()

# def meow():
#     print("Cats Meow")
# meow()

# def bray():
#     print("Donkeys bray")
# bray()

#Function Parameters
# def add_numbers(x,y): #A function for adding 2 numbers
#     sum_numbers= x+y
#     print(f"The sum of numbers is {sum_numbers}")
# add_numbers(40,34)
# add_numbers(40,67)
# add_numbers(90,64)

# def prod_numbers(x,y):
#     product_numbers= x*y
#     print("The product of numbers is ", product_numbers)
# prod_numbers(50,34)
# prod_numbers(384,28)
# prod_numbers(32,21029)

from math import sqrt

a = int(input("Enter the coefficient of first term (a)"))
b = int(input("Enter the coefficient of second term (b)"))
c = int(input("Enter the constant (c)"))
def find_roots(a,b,c):
    w= sqrt((b**2)-4 *a*c)
    y_1=int((-b + w) /(2*a))
    y_2=int((-b - w) /(2*a))
    print(f"The roots are {y_1} and {y_2}")
find_roots(a,b,c)