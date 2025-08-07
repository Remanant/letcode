print("Welcome to Roundabout Pizzas!!")
size = input("Please select your size - S, M or L: ").upper()
pepperoni = input(("Do you want pepperoni on thy pizza? Y for Yes and N for No: ")).upper()
cheese = input(("want extra cheese? Y or N:")).upper()
price = 15
           
#to get the correct input from the user
valid_input = (size in ['S','M','L'] and pepperoni in ['Y','N'] and cheese in ['Y','N'])    
if valid_input:
    if size == "S" and pepperoni == "Y": #if user choose pepperoni then +2
        price += 2
    elif size == "M": #if user choose med size then +5
        price += 5
        if pepperoni == "Y": #if user choose pepperoni then +3
            price += 3
    elif size == "L": #if user choose large size then +10
        price += 10
        if pepperoni == "Y": ##if user choose pepperoni then +3
            price += 3
    if cheese == "Y": #if user choose extra chees then +1 regardless of size 
        price += 1
    print(f"you choose {size} size pizza and the total would be {price} trillion won")
else:
    print("wrong input:")
    print("- size: S, M, or L")
    print("- pepperoni/cheese: Y or N")