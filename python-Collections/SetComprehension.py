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

diffResult = numSet1.symmetric_difference(numSet2)
print(diffResult) # 1,4,6,7,8,9

diffResult = numSet2.symmetric_difference(numSet1)
print(diffResult)

diffResult = numSet1.intersection(numSet2)
print(diffResult) # 2,3,5

diffResult = numSet2.intersection(numSet1)
print(diffResult)


diffResult = numSet1.union(numSet2)
print(diffResult)
diffResult = numSet2.union(numSet1)
print(diffResult)

