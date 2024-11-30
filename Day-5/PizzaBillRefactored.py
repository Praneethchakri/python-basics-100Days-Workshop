print("Welcome to Pizza - Python APP")

# User inputs
pizza_size = input("What type of Pizza do you want? S, M, L \n").upper()
want_pepperoni = input("Do you want Pepperoni on Your Pizza? Y or N \n").upper()
extra_cheese = input("Do you want extra Cheese on your Pizza? Y or N \n").upper()

bill = 0
if pizza_size == "L":
    bill +=25
elif pizza_size == "M":
    bill += 20
elif pizza_size == "S":
    bill +=15
else:
    print("Invalid Entry !! Please Refine your Search!!")


if want_pepperoni == "Y":
    if pizza_size == "S":
        bill +=2
    else:
        bill+=3


if extra_cheese == "Y":
    bill +=1


print(f"Your Bill Is Ready ${bill}.")