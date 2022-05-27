#1/usr/bin/python
rows= int(input("Enter the number of Rows "))
for i in range (rows):
    for j in range (i+1):
        print(j+1,end = " ")
    print("\n")