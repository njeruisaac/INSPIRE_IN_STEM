#1/usr/bin/python
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


colors=['red','green','blue','orange']

#With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i <len(colors):
    if(colors[0]=='red'):
        print(colors[0].upper())
        i +=1

i = 1
while i <len(colors):
    if(colors[1]=='green'):
        print(colors[1].upper())
        i +=1

i = 1
while i <len(colors):
    if(colors[2]=='blue'):
        print(colors[2].upper())
        i +=1

i = 1
while i <len(colors):
    if(colors[3]=='orange'):
        print(colors[3].upper())
        i +=1