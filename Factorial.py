#1/usr/bin/python
i = int(input("Enter the number "))
factorial = 1
if i < 0 :
    print("Factorial of negative number doesn't exist")
else :
    if i > 0 :
        for i in range (1,i+1):
            factorial= factorial*i
print("The Factorial of" ,i, "is" ,factorial,)