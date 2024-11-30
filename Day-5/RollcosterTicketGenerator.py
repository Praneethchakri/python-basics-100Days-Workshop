print("Welcome to the RollCoster!")
name = input("Please Tell Me your Name ?\n")
age = int(input("Tell me Your Age?\n"))
height = int(input("Please enter your Height? \n"))

if age < 12:
    if height == 100:
        print("Your Age does not Permit, But you are eligible because height meets the requirement")
        print("Please Sit with Your Parents !!! while doing rollerCoster")
        ticketPrice = int(3)
        print(f"Your Ticket Price is {ticketPrice} Euro's Only")
        wantPhotoTicket = input("Do you need Photo as well ?\n")
        if str(wantPhotoTicket) == str("Yes"):
            photoPrice = int(2)
            print(f"Photo Price {photoPrice} Euro's")
            totalSum = ticketPrice + photoPrice
            print(f"Total Price {totalSum}")
            print(f"Ticket ID: 85342")
        else:
            print(f"Total Price of RollerCoster Excl. PhotoTicket " + ticketPrice)
    else:
        print("Sorry Your are Age and Height are not eligible to do the rollercoster !! Try again Next Time Bye!!")
else:
    ridePrice = int(7)
    print("Before We print the Ticket , ")
    wantPhotoRide = input("do you want Photo of your Ride?'\n")
    if wantPhotoRide == str("Yes"):
        photoPrice = int(5)
        print("Your are an Adult !! Enjoy the Ride!")
        sumValue = ridePrice + photoPrice
        print(f"Total Final Price: {sumValue} Euro's")
        print(f"Ticket ID: 12345")
        print(f"Name: " + name + ", Height " + str(height))
    else:
        print("Your are an Adult !! Enjoy the Ride!")
        print(f"fYour Ride Price {ridePrice}")
