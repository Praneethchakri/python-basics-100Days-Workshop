# user_input = input("Enter p or q")
#
# while user_input != 'q':
#     if user_input == 'p':
#         print("Hello")
#
#
#     user_input = input("Enter P or Q")



tupleData = ('Praneeth','Charkvarthi')

print(tupleData[0])
tupleData = tupleData + ('Diguvapalem',)
print(tupleData)


listData = ['Dhoni','Mahendra','Singh']

listData.append("Indian")
listData.append("Captain")
listData.remove(listData[0])

print(listData)

setData = {'Ramesh','Sachin','Tendulkar'}

setData.add('God of ')
setData.add('Cricket')

print(setData)
cricData = {'Sachin','Dhoni','Kohli'}

famousCricNames = setData.difference(cricData)

print(famousCricNames)
commonData = setData.intersection(cricData)

print(commonData)

removeCommon = setData.symmetric_difference(cricData)
print(removeCommon)

unionData = setData.union(cricData)
print(unionData)