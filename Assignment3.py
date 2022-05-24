#1/usr/bin/python
#Print a diamond of stars and a pyramid of stars
# for numbers in numbers:
#     print(numbers**2)

#Half Pyramid
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()

#Full Pyramid
rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()

#Diamond
h = int(input("please enter diamond's height:"))

for i in range(1, h, 2):
    print(" "*(h//2-i//2), "*"*i)
for i in range(h, 0, -2):
    print(" "*(h//2-i//2), "*"*i)