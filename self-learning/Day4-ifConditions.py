name = 'Dhoni'

userInput = input("Enter Your Name::")

if userInput == name:
    print(f"Hello ! {userInput}")
    print("How are You? ")
else:
    print(f"Hello Stranger!! {userInput}")

for i in range(10):
    if bool(i):  # All the numbers are True except 0
        print(f"True: {i}")
    else:  # Except  0 all the numbers are True
        print(f"False: {i}")

friendsList = ['Anil', 'Adeeb', 'Konda']
familyList = ['ChandraSekhar', 'Nagamani', 'Sarvani', 'Sushma', 'Prajna']

userInput = input("Enter Your Name:: ")

if userInput in friendsList:
    print(f"Hello ! Friend {userInput}")
elif userInput in familyList:
    print(f"Hello Family: {userInput}")
else:
    print(f" Hello Stranger :: {userInput}")
