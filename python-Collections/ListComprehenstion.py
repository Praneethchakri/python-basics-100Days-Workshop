age_List = [25,63,85,12]
oddAge = []

result  = [age for age in age_List if age % 2 == 1]
print(result)


friends = ['Praneeth','Ramesh','Suresh','Hareesh']
guest = ['Kumar','Suresh','Praneeth']


attendList = [frnd for frnd in friends if frnd in guest]

print([f'Party Attended Friends are {f}' for f in attendList])
