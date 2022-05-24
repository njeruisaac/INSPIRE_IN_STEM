#Program to withdraw 25k if the acc is between 100k and 200k or 30% if acc is between 500k and 1M
acc_bal = int(input("What is your account balance?"))
if (acc_bal > 100000) and (acc_bal<200000):
    acc_bal = acc_bal - 25000
    print(f"Your account has been deducted 25000. Account balance is{acc_bal}")
else:
    if(acc_bal>500000) and (acc_bal<1000000):
        acc_bal = acc_bal - (acc_bal*0.3)
        print(f"You account has been deducted 30%. Account balance is{int(acc_bal)}")
