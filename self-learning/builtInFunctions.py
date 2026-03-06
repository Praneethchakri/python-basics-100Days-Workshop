# abs(): it returns the absolute value of a number
# all(): It  returns true if all the items  in  an iterable objects are true.
# any(): It Returns true if any of the item in an iterable ojbect is true
# ascii() :Returns a readable version of an object . Replaces non ascii chars with escape character
# bin(): returs the binary version of a number
# bool(): Returns the boolean value of the specified object

value = (1,3,4,5,6,False)
if any(value):
    print(ascii(value))
else:
    print('else ')

print(abs(123))

print(f'''list of builtin functions 
* max()
* min()
* len()
* round()
* int()
* str()
* sum()
* print()
* range()''')

