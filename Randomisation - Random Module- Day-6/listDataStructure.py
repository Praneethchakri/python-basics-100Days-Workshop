# List Data Structure
# Syntax
#  eg: listData = [item1,item2]
from this import s

fruits = ['Cherry', 'Apple', 'Orange',1213,123.12]

print(fruits[-3]) # ndexError: list index out of range
#negative indexs is will go in reverse order to find the element
# -1 refer to 123.12
# -2 refer to 1213
# -3 refer to orange

fruits[0] = 'Mango'
for s in fruits:
    print(s)

fruits.append('straberry')

for s1 in fruits:
        print(s1)




