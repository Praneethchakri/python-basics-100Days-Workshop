
operations={
    "avg" : lambda seq :sum(seq)/len(seq),
    'max' : lambda seq:max(seq),
    'total' : lambda seq : sum(seq)
}


students = [
    {'name':'Praneeth','grades':{100,43,23,42,32,56}},
    {'name': 'Praneeth', 'grades': {100, 43, 23, 42, 32, 56}},
    {  'name': 'Praneeth', 'grades': {100, 43, 23, 42, 32, 56}}
]


for student in students:
    print(student)