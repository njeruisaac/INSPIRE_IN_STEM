#1/usr/bin/python

##
#   Dictionaries
#   Name: Isaac Njeru
#   Date: 23/5/2022

student = {"Name":"Isaac","Age": "20","Gender":"Male"}
student["Id Number"]= "39277231"
student["Hobbies"]="Music Production"
student["Favourite Color"]="Black"
student["Favourite Meal"]="Chapati"
print(student["Name"])
print(student["Age"])
print(student["Gender"])
print(student["Hobbies"])
print(student["Favourite Color"])
print(student["Favourite Meal"])

#Initialise an empty dictionary
# variable={}(calibraces)
student={}
student["homeCity"]="Nairobi"
student["preferredSport"]="Rugby"
student["instrumentPlayed"]="Piano"
student["Name"]="Jeff"
del student["Name"]
print(student)

#Lopping in dictionary
person = {
    'Name':'Isaac',
    'Address':'Thome',
    'Gender':'Male',
    'Number':'0787066143', 
}
print(person)
for key,value in person.items():
    print(f"{key}:{value}")