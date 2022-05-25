acc_bal = int(input("What is your account balance?"))
if (acc_bal > 100000) and (acc_bal<200000):
    acc_bal = acc_bal - 25000
    print(f"Your account has been deducted 25000. Account balance is{acc_bal}")
elif(acc_bal< 100000)  :
    print(f"Your account balance is still {acc_bal}")
elif(acc_bal>500000) and (acc_bal<1000000):
        acc_bal = acc_bal - (acc_bal*0.3)
        print(f"You account has been deducted 30%. Account balance is{int(acc_bal)}")
else:
    print(f"Your account balance is below the required amount. Account balance is {acc_bal}")