
from datetime import date
today = date.today()
Today=today.day
Year=today.year
Month=today.month

print("enter the product expiry date : ")

exp_year = int(input("enter the expiry year : "))
exp_month = int(input("enter the expiry month : "))
exp_date = int(input("enter the expiry date : "))

if (exp_year >= Year):
    if  (exp_month >= Month):
        if (exp_date >= Today):
            print("Food is Edible.")    
        else:
            print("Food is Expired!.")
    else:
        print("Food is Expired!.")
else:
    print("Food is Expired!.")
    


