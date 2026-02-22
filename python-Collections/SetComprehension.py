friends = ["Rajesh", "Suresh", "Haressh", "Kumar"]
guests = ["Kumar", "Rajesh", "Arun", "Pankaj"]

friendsSet = {f.lower() for f in friends}
guestsSet = {f.lower() for f in guests}

present_friends = friendsSet.intersection(guestsSet)

present_friends = {pf.title() for pf in present_friends}
print(present_friends)

numSet1 = {1, 2, 3, 4, 5, 6}

numSet2 = {2, 3, 5, 7, 8, 9}

# position of Set is importent before access the functions
diffResult = numSet1.difference(numSet2)
print(diffResult) # 1,4,6

diffResult = numSet2.difference(numSet1)
print(diffResult) # 7 8,9

sym_diffResult = numSet1.symmetric_difference(numSet2)
print(diffResult) # 1,4,6,7,8,9

sym_diffResult = numSet2.symmetric_difference(numSet1)
print(diffResult)

interSectionResult = numSet1.intersection(numSet2)
print(diffResult) # 2,3,5

interSectionResult = numSet2.intersection(numSet1)
print(diffResult)


unionResult = numSet1.union(numSet2)
print(diffResult)
unionResult = numSet2.union(numSet1)
print(diffResult)


#directly assinged data to Set

nameSet1 = {"Praneeth","Chakravarthi","Diguvapalem","Chakri"}

nameSet2 = {"Chakravarthi","Diguvapalem","PrajnaSri","Sushma"}


diff_Result = nameSet1.difference(nameSet2)
print(diff_Result) #Praneeth,Chakri

diff_Result = nameSet2.difference(nameSet1)
print(diff_Result) # PrajnaSri,Sushma


sym_diffResult = nameSet1.symmetric_difference(nameSet2)
print(sym_diffResult)#Praneeth,Chakri,PrajnaSri,Sushma

interSectionResult = nameSet1.intersection(nameSet2)
print(interSectionResult) # Chakrvarthi,Diguvapalem

unionResult  = nameSet1.union(nameSet2)
print(unionResult) # all data,except duplicate as set not allows

# list to Set with comprehension


friendsList = ["Praneeth","Chakravarthi","Diguvapalem","Chakri"]

guestList   = ["Chakravarthi","Diguvapalem","PrajnaSri","Sushma"]


friendsSet = {f.lower() for f in friendsList}
guestsSet  = {g.lower() for g in guestList}

attendess = friendsSet.intersection(guestsSet)
unattenedFriends = friendsSet.difference(guestsSet)

print(f'Unattended Friends ',{result.title() for result in unattenedFriends})
print({result.title() for result in attendess})





