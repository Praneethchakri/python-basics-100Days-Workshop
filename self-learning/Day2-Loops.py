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



# Dictionaries Data Type with key value pair model

family_Details = {'Praneeth':33,'Sushma':31,'PrajnaSri':5}

print(family_Details['Praneeth'])
family_Details['Dhoni']=43
family_Details['Sushma']=32
print(family_Details)


crickters = (
    {"name":'Dhoni',"age":43}, # inside tuple we have 3 dictionaries
    {"name": 'Sachin', "age": 53},
    {"name": 'Rahul', "age": 33},
)

crickters = crickters+({'name':'Sehwag','age':48},)
print(crickters)

print(crickters[1]["name"])
print(crickters[2]["age"])


# if we have a list of tuples , to covert to dictonaries

cric = [('Praneeth',3),('Sushma',2),('Saravani',3)]

cricDictonaries = dict(cric)

print(cricDictonaries)