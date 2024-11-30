print("Welcome to RollerCoster Ride Ticket App")

height = int(input("Enter your Height!!!\n"))
age = int(input("Please enter your Age!!!\n"))
photo = input("Do you want photo of your Ride \n")

ticket = 0;

if height < 120:
    print("Your are not eligible to Ride the rollerCoaster!!! Sorry")
    exit(0)
else:
    print("You can Ride!!!")
    if age < 12:
        ticket += 5
    elif 18 > age >= 12:
        # age <18 and age >=12:
        ticket += 7
    elif 45 <= age <= 55:  # 33 >= 45 F && 33 >= 55 F
        # age >= 45 and age <= 55:
        ticket += ticket
    else:
        ticket += 12

if photo == "Y":
    ticket += 3
else:
    ticket

print(f"Ticket Price {ticket}")

