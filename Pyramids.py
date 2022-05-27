#1/usr/bin/python
rows= int(input("Enter the number of Rows "))

# for i in range (rows):
#     for j in range (i+1):
#         print(j+1,end = " ")
#     print("\n")
k=0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()