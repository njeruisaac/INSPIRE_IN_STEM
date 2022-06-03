#1/usr/bin/python
import random
print("Welcome to our Password Generator")
character="Njeru2129"
num_password= int(input("How many passwords would you like to create "))
pass_length= int(input("How many characters would you like? "))
for password in range(num_password):
    password=''
for c in range(pass_length):
    password +=random.choice(character)
print(password)

##Ask user for number of passwords they want to generate
#Convert password to integer
#Ask user for password length
#Convert len password to integer