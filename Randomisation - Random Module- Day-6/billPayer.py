import random

friends = ["Praneeth" , "Sushma" , "PrajnaSri"]
# choice function which takes sequence as input, to pick the random value from list data structure
# 1 option
billPayer = random.choice(friends)
print(billPayer)
print(len(friends))
# 2 option
random_FriendIndex = random.randint(0, len(friends)-1)
print(friends[random_FriendIndex])
