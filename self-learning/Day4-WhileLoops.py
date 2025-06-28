userInput = input("Do you want to study well and understand the python? Yes or No")

while userInput == 'Yes':
    print("Good...Let's Focus... on it")
    userInput = input("Still do you have focus.... Yes or No")
print("Ok.. Take a Break!!! ComeBack Soon..")

listOfDict = [
    {'name': 'Praneeth', 'age': 33},
    {'name': 'Sushma', 'age': 31},
    {'name': 'PrajnaSri', 'age': 5},
    {'name': 'P', 'age': 100}
]

# Practicing for Loop As Well...
for person in listOfDict:
    name = person['name']
    age = person['age']

    print(f'''{name} is {age} year's old''')

list = [
    ('Albert', 'Scientist', 'Germany', 89),
    ('James', 'Scientist', 'Germany', 99),
    ('Grahambell', 'Scientist', 'France', 79)
]

for name, profession, country, age in list:
    print(f'{name} is a Great {profession} from {country} and {name} age is {age}')
