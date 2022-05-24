age = int(input("What is your age?"))
user_gender=input("What Gender are you?")

acc_bal = 209 

if (age >25) and (age<30):
    acc_bal = acc_bal + 10000
    print(f"Confirmed your account balance is {acc_bal} ")
else:
     print("You are not eligible for the funds")