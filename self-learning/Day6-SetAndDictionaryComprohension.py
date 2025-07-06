indianTeam = {'Sachin', 'Rahul', 'Ganguly', 'Yuvraj', 'Kaif', 'Dhoni'}

reserveBench = {'Sehwag', 'Zaheer', 'Nehra', 'Rahul', 'Dhoni'}

# difference method ->unique elements from the Set and ingorning the common elemtns

result0 = reserveBench.difference(indianTeam)
print(result0)

# symmetric_difference - Excluding the common element from both the sets ,and remaining result as a seperate Set
result1 = reserveBench.symmetric_difference(indianTeam)
print(result1)

# intersection -> only common elements in both sets as a seperate Set

result2 = reserveBench.intersection(indianTeam)
print(result2)

# union - > merge both the sets and avoid the duplicates
result3 = reserveBench.union(indianTeam)
print(result3)

jersyNumber = {1, 99, 7, 18, 10, 45}

reservedJerseyNumbers = {7, 10}

result4 = jersyNumber.intersection(reservedJerseyNumbers)  # intersection will give the common elements
print(result4)  # 10,7

result5 = jersyNumber.difference(reservedJerseyNumbers)  # only numbers from the main set avoid the duplicates
print(result5)  # 1,99,18,45

result6 = jersyNumber.symmetric_difference(reservedJerseyNumbers)  #
print(result6)  # 1,99,18,45,

result7 = jersyNumber.union(reservedJerseyNumbers)
print(result7)  # 1,99,7,18,45,10
