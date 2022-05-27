#1/usr/bin/python
a= int(input("Enter the first number "))
d= int(input("Enter the common difference "))
n = int(input("Enter the number of terms "))
for i in range (1,n+1):
    n_am = a + (i-1)*d
    print(n_am)
sum_n = (n_am/2)*(2*a+(n-1)*d)
print("Sum of Arithmetic progression is", int(sum_n))