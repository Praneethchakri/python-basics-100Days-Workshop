
#enumarate
friends = ["Praneeth","Diguvapalem","Chakravarthi"]
print(f" enumerate function in python is used to add a number to the element in a list and returns as {list(enumerate(friends))} , list of tuples in a list")

# old way/ unused way
index = 0
print("way-1")
for f in friends:

    print(f)
    print(index)
    index = index+1


# way2
print("way-2"),# start parm to start the counter number from assined value
for counter ,f in enumerate(friends,start =4):
    print(counter)
    print(f)

# Way3
print(list(enumerate(friends))) # as List of tuples [(0, 'Praneeth'), (1, 'Diguvapalem'), (2, 'Chakravarthi')]

print(dict(enumerate(friends))) # as Dictionary , key and value  pair