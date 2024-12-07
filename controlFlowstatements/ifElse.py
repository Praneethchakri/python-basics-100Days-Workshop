print("Python :: if Else Conditions in Python")

gender = str(input("Enter your Gender ::\n"))
if gender == "M":
    print("Male")
else:
    print("FeMale")

print("Python :: Nested if Else conditions  in python")
age = int(input("Please Enter Age :: \n"))

if age <= 33:
    print(" Young Age....")
elif 34 >= age <= 50:
    print("Middle Age")
else:
    print("Old Age")

print("Python :: For Loop Statements::")

family = ["Praneeth", "Sushma" , "Prajna" , "Amma" , "Nana"]
for name in family:
    print("Name:: "+name)


# count = range(10)
i = 0
for i in range(13):
    print("I value "+str(i))
    if i <= 10:
        print("Count of i in if Condition "+str(i))
        i = i+1
    elif i >= 10:
        print("Count of i is "+str(i))


print(" Python :: Nested Forloops::")
for i in range(3):
    for j in range(2):
        print(f"{i} {j}")


for i in range(5):
    for j in range(3):
        for k in range(2):
            print(f"{i} {j} {k}")
