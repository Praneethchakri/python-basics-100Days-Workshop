print("Welcome To Python Pizza Billing App")

# User inputs
pizza_size = input("What type of Pizza do you want? S, M, L \n").upper()
want_pepperoni = input("Do you want Pepperoni on Your Pizza? Y or N \n").upper()
extra_cheese = input("Do you want extra Cheese on your Pizza? Y or N \n").upper()

# Pizza prices
S = 15
M = 20
L = 25
bill = 0

# Extra costs
extra_cheese_cost = 1


# Calculate bill
if pizza_size == 'L':
    bill = L
    # print(f"Large Pizza: ${bill}")
    if want_pepperoni == 'Y':
        bill += 3
        # print(f"Large Pizza with Pepperoni: ${bill}")
    if extra_cheese == 'Y':
        bill += extra_cheese_cost
        # print(f"Large Pizza with Extra Cheese: ${bill}")
elif pizza_size == 'M':
    bill = M
    print(f"Medium Pizza: ${bill}")
    if want_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += extra_cheese_cost
else:  # Assuming the default is Small pizza
    bill = S
    # print(f"Small Pizza: ${bill}")
    if want_pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += extra_cheese_cost

# Final Bill
print(f"Total Bill: ${bill}")
print("Enjoy your Pizza!!")
