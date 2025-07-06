indianTeam = {'Sachin','Rahul','Ganguly','Yuvraj','Kaif','Dhoni'}

reserveBench = {'Sehwag','Zaheer','Nehra','Rahul','Dhoni'}


#difference method ->unique elements from the Set and ingorning the common elemtns

result0 = reserveBench.difference(indianTeam)
print(result0)

#symmetric_difference - Excluding the common element from both the sets ,and remaining result as a seperate Set
result1 = reserveBench.symmetric_difference(indianTeam)
print(result1)

#intersection -> only common elements in both sets as a seperate Set

result2 = reserveBench.intersection(indianTeam)
print(result2)

#union - > merge both the sets and avoid the duplicates
result3 = reserveBench.union(indianTeam)
print(result3)

