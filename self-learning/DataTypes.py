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


print("Set Methods ")

arts_students ={"Ramesh","Suresh","Kamal","Pramod"}
science_Studnets = {"Pramod","Charan","Praneeth"}

arts_students_not_in_Science = arts_students.difference(science_Studnets)
print(arts_students_not_in_Science)
science_Studnets_not_in_arts = science_Studnets.difference(arts_students) # difference is to remove the commen element in both sets
print(science_Studnets_not_in_arts)

arts_students_in_Science_both = arts_students.symmetric_difference(science_Studnets) #symetric_difference is to remove the common element in both the sets
# and make one commone set
print(arts_students_in_Science_both)
arts_students_in_Science_both_intersection = arts_students.intersection(science_Studnets) # intersection method is used to find the common element from both sets
print(arts_students_in_Science_both_intersection)

arts_students_in_Science_both_union = arts_students.union(science_Studnets)
print(arts_students_in_Science_both_union) # union method remove the duplicates and combine both sets




batsmen = {"Dhoni","Sachin","Rahul","Yuvraj"}
bowler = {"Zaheer","Jadeja","Yuvraj"}
batsmenOnly = batsmen.difference(bowler)

print(batsmenOnly)

bowlerOnly = bowler.difference(batsmen)
print(bowlerOnly)

allRounder = bowler.intersection(batsmen) # common  element from both sets
print(allRounder)

print(bowler.symmetric_difference(batsmen)) # common element in both sets will be removed..

unique_Players = bowler.union(batsmen)
print(unique_Players) ## By removing the duplicates and keep  all the disticnt values

setdata = {"Ram","Sures"}
setdata.add("Charan")
print(setdata)