tuple_data=('Praneeth','Ramesh','Suresh')

print(tuple_data)

# tuple_data.append("Raja")
"""("Raja") will be considered as String , if we miss  a 'comma , 'at the end of string .."""

tuple_data = tuple_data+("Raja",)
print(tuple_data)

""" Here List Data type which can be modified by adding using append method or removing

List is modifieble , where as Tuple is not modifieble
"""
list_Data = ["Praneeth",'Charkvarthi','Dhoni']

list_Data.append("MS")
print(list_Data)
list_Data.remove(list_Data[0])
print(list_Data)



"""Set Data Type , doesnt hold the order of elements and doesn't allow duplicates

Set Data structure will be stored in curly brackets ,Sets are used to compare the data btw two sets , liek uniqued and diff elements in sets
"""

set_DataType = {"Rama","Sita","Lakshmana"}
print(set_DataType)


set_DataType.add("Hanuma")

print(set_DataType)


