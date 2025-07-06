print("List Comprehension with Strings")
friendList = ['Dhoni', 'Sachin', 'Sehwagh', 'Yuvraj']

guestList = ['Kohli', 'Rohit', 'Rahul', 'Praveen', 'Sachin', 'Dhoni']

friendList_toLower = [friend.lower() for friend in friendList]

bestFriends = [guest.title() for guest in guestList if guest.lower() in friendList_toLower]

print(bestFriends)


print("List Comprehension with Numbers")
number = [1, 4, 3, 2, 5, 7, 45]

oddNumber = [oddnum for oddnum in number if oddnum % 2 == 1]

print(oddNumber)
