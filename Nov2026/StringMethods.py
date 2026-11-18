name = "Harry"
print(len(name))

print(name.upper())
print(name.lower())


name = "praneeth charkvarthi diguvapalem"

print('''# caplitalize , converts the first character to Capital
# title, converts every character to capital after space''')
print(name.capitalize())

print(name.title())


user = " praneeth "
print('''#strip, rstrip(),lstrip()''')
print(user.strip())

print(user.lstrip())

print(user.rstrip())


print('''# find() gives the positon of string ,)
# replace() , overrides the string with new String''')

print("\n")

sentance1 = "Python is a Language"

print(sentance1.find("Language"))
print(sentance1.replace("Language","Programming Language"))