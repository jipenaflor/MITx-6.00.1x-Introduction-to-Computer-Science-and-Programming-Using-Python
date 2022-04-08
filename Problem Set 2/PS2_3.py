#The following variables contain values as described below:
    #balance - the outstanding balance on the credit card
    #annualInterestRate - annual interest rate as a decimal
    #Monthly interest rate = (Annual interest rate) / 12.0
    #Monthly payment lower bound = Balance / 12
    #Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
#Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent (no more multiples of $10)
#such that we can pay off the debt within a year.

monthlyInterestRate = annualInterestRate/12
lbound = balance/12
hbound = (balance*((1+monthlyInterestRate)**12))/12

def checker(bal, mInterest, low, high):
    mid = (low + high)/2
    payment = round(mid, 2)
    for m in range(12):
        bal -= payment
        bal += (mInterest)*bal
    if round(bal, 2) > 0.10:
        return checker(balance, mInterest, payment, high)
    elif round(bal, 2) < -0.10:
        return checker(balance, mInterest, low, payment)
    else:
        return payment

minMonthlyPayment = checker(balance, monthlyInterestRate, lbound, hbound)
print("Lowest Payment: ", minMonthlyPayment)
