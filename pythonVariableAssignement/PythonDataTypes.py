print("Python Data Types: Mutable, Immutable")

print("Under Immutable Data Types: "
      "String,Numbers, Tuples")
print("Under Mutable DataTypes:: "
      "Lists,Dictionaries,Sets")

print("Number Data Types: ")
x =10
y = 23.2
# z = 1232232132L Python 2 its valid
z = 12342324  # from python 3.10 onwards no trainling L for Long
# From version Python 3.10 on wards the trailing L has been removed , only one data type as int
print(f"{x}: {type(x)}, {y}:: {type(y)}, {z} : {type(z)}")
print("Type function to show the data Type as Above")


print("String Data Type")
print("Which is written under single,Double quotes considerd as String")
str1 = "Hello! World!!!"
str2 = "Python"
print(f"{str1} :: First Char:: {str1[0]}")

print(f"{str2} :: Last Char:: {str2[-1]}")

print(f"{str1[0:5]}")# 5 char will not be consider while looking for 4 char word, base rule ..

print(f"{str1[7:12]}")
print(f"{str2[-6]}")

print("Function of Strings:  find()")
print(f"{str1.find('Wo')}")
print(f"{str1.find('ll')}")

print("Function of Strings:: replace()")
str1 = str1.replace('World','Python World')
print(f"{str1}")
print(str1)

print(str2.replace("on","ON"))

print("Function of Strings: split()")
str1 = str1.split("!")
print(str1)

str3 = 'Praneeth Charkvarthi Diguvapalem'

str3 = str3.split('a') # once we split the string it convert the type to List, to access index basis
print(f"{str3}")

print("Function of Strings: count()")
str4 = "Praneeth"
str5 = "PRANEETH"
print(str4.count('e'))
print("Function of Strings: upper(),lower()")
print(f"{str4.upper()}")
print(f"{str5.lower()}")

print("Function of Strings : min(),max() ASCII value of chars to find in a string")
print(max(str5))
print(min(str5))
randomString = "!@#$werwZz"
print(max(randomString))
print(min(randomString))


print(f"String methods: count(),split(),min(),max(),replace(),find(),upper(),lower()")