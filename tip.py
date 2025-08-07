//a calculator to calculate the amount of bill you have to give if you happen to go outside 

print("welcome to the tip calculator.")
total_bill = float(input("whats yout total bill? $"))
tip_amount = float(input("percentage amount of tip you want to give?"))
if tip_amount == 0:
    print("you are stingy")
persons = int(input("total amounts of peers you got?"))

bill_amount = tip_amount/100 * total_bill + total_bill
round(bill_amount, 2)
if persons == 0:
    print("loner ass")
    print(f"you will have to pay {bill_amount}")
if persons > 0:
    print(f"you will have to pay {bill_amount/persons}") 
