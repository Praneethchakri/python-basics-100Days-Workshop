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
family = ["Praneeth", "Sushma", "Prajna", "Amma", "Nana"]
for name in family:
    print("Name:: " + name)

# count = range(10)
i = 0
for i in range(13):
    print("I value " + str(i))
    if i <= 10:
        print("Count of i in if Condition " + str(i))
        i = i + 1
    elif i >= 10:
        print("Count of i is " + str(i))

print(" Python :: Nested Forloops::")
for i in range(3):
    for j in range(2):
        print(f"{i} {j}")

for i in range(5):
    for j in range(3):
        for k in range(2):
            print(f"{i} {j} {k}")

print("Python :: While Loop ")

x = 1
while x < 5:
    print(x)
    x += 2

i = 0
while i < 10:
    if i % 2 == 0:
        print(f"{i} is Even Number")
    else:
        print(f"{i} is Odd Number")
    i += 1

print("Python :: break Statement")
print("once a vale reaches as 5 , else enterd and break executed")
a = 10
while a > 0:
    if a != 5:
        print(a)
    else:
        break
    a -= 1

print("Python :: Continue Statement")

print("Python :: Continue Statement")

x = 10
while x > 0:
    if x == 5:
        # Skip printing and decrementing for this case
        x -= 1
        continue
    elif x == 2:
        # Skip directly to the next iteration without decrementing
        x -= 1
        continue
    elif x <= 5:
        print(f"{x} ")
    else:
        print(f" {x}  <--> Value ")
    x -= 1




