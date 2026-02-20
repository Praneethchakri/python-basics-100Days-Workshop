friends = ["Rajesh","Suresh","Haressh","Kumar"]
guests = ["Kumar","Rajesh","Arun","Pankaj"]

friendsSet = {f.lower() for f in friends}
guestsSet  = {f.lower() for f in guests}

present_friends = friendsSet.intersection(guestsSet)

present_friends = {pf.title() for pf in present_friends}
print(present_friends)

