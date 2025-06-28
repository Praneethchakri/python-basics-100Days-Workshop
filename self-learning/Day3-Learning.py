# list,tuple,set,Dictionaries

list_Data = ['Science', 'social', 'Maths', 'History', 'Biolagy', 'Telugu', 'English']
# forloop

list_Data.append("Deutsche")  # add the element at the end.
list_Data.remove(list_Data[0])  # remove the element
# list_Data.insert(0,'Hindi') # insert to insert an element in particualr index of a list
print(list_Data)
print("!!!!!!!!!!!!!!!!!!!!!")
list_Data.extend(['Hindi', 'Hindi2', 'Hindi3', 'Hindi4'])
for s in list_Data:
    print(s)

print("Sublist items ")
print(len(list_Data))
print(list_Data)

for subList in list_Data[0]:
    print(subList)

for i in range(10):
    list_Data.append(i)
print(list_Data)

for i in range(100, 200):  # it will append all the numbrs in the range
    list_Data.append(i)

print(list_Data)

list_Data.reverse()  # self reverse the list
print("Check")
print(list_Data)

listData = ['one', 'Two', 'Three', 'Four', 'Five']
for index, s in enumerate(listData):
    print(index, s)

# Set


setData = {'SetData1', 'SetData2', 'SetData3', 'SetData4'}

print("Set data interating....")  # order will not be maintained..
for s in setData:
    print(s)

print("\n")
setData.add("SetData5")
setData.add("SetData6")
setData.add("SetData7")

for s in setData:
    print(s)

setData.remove('SetData5')  # remove the specified data from set , if not exist , throw the KeyError:
# print(setData)
print("\n")

setData.discard('SetData10')  # if element doesnot exist will not throw error instead will show the existing data
for s in setData:
    print(s)

setData.pop()  # pop method will remove the random element from the Set
print("\n")
for s in setData:
    print(s)

setData.clear()  # remove all the elements from the list.

if len(setData) > 0:
    for s in setData:
        print("test", s)
else:
    print("Empty Set Here..")

# tuple data Type
tupleData = ('Praneeth', 'Diguvapalem', 'Chakravarthi')
print("\n")
print(
    "Printing Tuple Data:: data will be stored in ()  Tuple cannot modify once we create , but can append data by addding in below syntax ")
for s in tupleData:
    print(s)

tupleData = tupleData + ('AddingAnother Element ',)
for s in tupleData:
    print(s)

# dictionaries
myDictionaries = {'Praneeth': 'Male', 'Sushma': "Female", 'PrajnaSri': 'Female'}

print(myDictionaries.get('Praneeth'))
myDictionaries['Praneeth'] = "MALE"  # Updated the value using index data
print(myDictionaries)

# a tuple() contains multiple dictionaries{},{},{} and a list[] contains multiple tuples (),(),()
# tuple Contains three dictionaries
tupleDict = (
    {'name': 'Sachin', 'age': 10},
    {'name': 'Dhoni', 'age': 7},
    {'name': 'KapilDev', 'age': 21}
)
tupleDict = tupleDict + ({'name': 'Rohit', 'age': 45},)

print(tupleDict[1]['name'] + " " + str(tupleDict[1]['age']))

# dictionary = dict(tupleDict)

# print(dictionary)
for d in tupleDict:
    print(d)

listTuple = [('sachin', 54), ('Dhoni', 43), ('KapilDev', 65)]

print(listTuple)
listTupleToDictionary = dict(listTuple)
print(listTupleToDictionary)
print(len(listTupleToDictionary))

for dictionaryDataKey, Value in listTupleToDictionary.items():
    print(dictionaryDataKey, Value)

for index, key in enumerate(listTupleToDictionary):
    print(index, key, listTupleToDictionary[key])

for key, value in listTupleToDictionary.items():
    print(key, value)

listJoin = ['Deutsche Bank', 'Commerz Bank', 'Bank of America']

seprateListBySpcialChar = ','.join(listJoin)
print(f'''Bank Name's i Know {seprateListBySpcialChar}''')
