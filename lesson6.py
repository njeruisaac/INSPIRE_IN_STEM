#Lists : Use box brackets / Has index / single quotes
motorcyle = ['Yamaha','Ducatti','Honda']
plate_number = [' Y123\n',' D123\n',' H123',]
motorcyle_owner = "Harvey Specter"
print (motorcyle)

#Accessing list items using index
print(motorcyle[3])

#Changing element in a list
motorcyle[1] = 'Ducatti'
print("I love " + str(motorcyle[1]))

#Add Item into a list .append('')
motorcyle.append('Navi')
print(motorcyle)


print(motorcyle[0] + plate_number[0], motorcyle[1]  + plate_number[1], motorcyle[2] + plate_number[2])
#Working with Lists
#Loops: While / For

#Delete item from list
del motorcyle[1]
print (motorcyle)

#Delete item from list method 2
popped_motorcycle= motorcyle.pop()
print(motorcyle)
print(f"My name is {motorcyle_owner} and I own a {motorcyle[1]} motorcyle {plate_number[1]}")

#Removing an item from a list
motorcyle.remove('Yamaha')
print(motorcyle)