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

    # This line loads a set of 6 random numbers from the config file
    # lottery_numbers = config.lottery_numbers

    # Here are your players; find out who has the most numbers matching lottery_numbers!
    players = [
        {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
        {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
        {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
        {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
    ]

    # Then, print out a line such as "Jen won 1000.".
    # The winnings are calculated with the formula:
    # 100 ** len(numbers_matched)


print(players)





















