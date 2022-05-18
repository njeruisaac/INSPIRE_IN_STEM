#Slice 
city = "Nairobi"
print(city[:5])
print(city[:3])
print(city[:-2])

#UpperCase
f_name = "isaac"
#.upper() convert to upper case
print(f_name.upper() )

#LowerCase
s_name = "NJERU"
print(s_name.lower())

#Concatenation of data types
#Float(numeral numbers with decimal points)...float(x)

#int to string
number = 7
print(str(number))

#int to float
x = 4 #x is an integer
print(float(x))

#float to int
v =3.24
print(int(v))

first_name = "Isaac"
second_name = "Njeru"
full_name = first_name + second_name
print(full_name)

#Replacing Characters
print(full_name.replace('a','p'))

#Splitting lines
msg1 = "Hello Weclome to Tumba How may we assist you"
print(msg1.split())

print(len(msg1))