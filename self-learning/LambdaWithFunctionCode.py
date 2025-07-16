operations = {
    "avg": lambda seq: sum(seq) / len(seq),
    'max': lambda seq: max(seq),
    'total': lambda seq: sum(seq)
}

students = [
    {'name': 'Praneeth', 'grades': {100, 43, 23, 42, 32, 56}},
    {'name': 'Suresh', 'grades': {89, 22, 23, 42, 32, 56}},
    {'name': 'Mahesh', 'grades': {99, 23, 23, 42, 32, 56}}
]

for student in students:

    name = student['name']
    grade = student['grades']
    print(f'Student Name: {name}')
    operation = input("User Input as Avg or Max or total")

    action = operations[operation]
    print(action(grade))

