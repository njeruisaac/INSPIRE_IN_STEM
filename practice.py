#1/usr/bin/python
# def get_sum(num_1,num_2):
#     sum_num= num_1 + num_2
#     return sum_num
# print(get_sum(9,10))

# def get_to_power(num_1,power):
#     power= num_1**power
#     return power
# print(get_to_power(6,4))

# def print_full_names(f_name,s_name):
#     full_name= str(f_name )+ str(s_name)
#     return full_name.title()
# print(print_full_names("isaac ","njeru"))

#Returning a dictionary from a function
# def create_full_name(first_name,second_name):
#     person={'first':first_name, 'second':second_name}
#     return person
# student=create_full_name("Bob","Afwata")
# print(student)

#Parsing lists in a function
def greet_friends(names):
    for name in names:
        msg= "Hello " + str(name.title())
        print(msg)
friends=['Maggie','Freddie','Jeff','Sam','James','Chris','Lisa']
greet_friends(friends)