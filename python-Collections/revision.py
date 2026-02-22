family = ["One","Two","Three","Four"]
friends = ["Five","Four","One","Three"]

famSet = set(family)
friSet = set(friends)

# print(f"{famSet} , {friSet}")

diff = famSet.difference(friSet)# diff value from familySet
print(diff)

diff = friSet.difference(famSet) #five
print(diff)

sym_diff = famSet.symmetric_difference(friSet)
print(sym_diff)

union = famSet.union(friSet)
print(union)

intersection = famSet.intersection(friSet)
print(intersection)


zipResult = list(zip(family,friends))
print(zipResult)


for zr in enumerate(zipResult,start=1):
    print(zr)
