# # Python Variables – Assigning Values
# #
#
# a = 10
# name = "Praneeth"
# salary = 2034324.2
#
# print(a)
# print(name)
# print(salary)
#
# a = b = c = 7
# x, y, z = 10, 20, 30
#
# print(a)
# print(b)
# print(c)
# print(x)
# print(y)
# print(z)
#
# # Integer
# i = 10
# print(i)
# print(type(i))
#
# # Float
# f = 10.09
# print(type(f))
#
# # Boolean
# flag = True
# print(type(flag))
#
# # String
# stringData = "TESTingString"
# print(type(stringData))
#
# for name in range(0, 100):
#     print(name)
#
# c = 0
# while c < 100:
#     print(c)
#     c += 1

numberTable = 2
counter = 1
middle_number = 1
for number in range(2,10):
    for counter in range(1,11):
        print(f'{number} * {counter} = {number*counter}')
    print()


user_names = list()
print(type(user_names))

user_names.append("Praneeth")
user_names.append("Chakravarthi")

print(user_names)
user_names.pop(0)
print(user_names)
user_names.pop()
print(user_names)