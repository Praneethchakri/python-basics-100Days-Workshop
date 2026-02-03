print("Tuples:: Characterstics")
print('''1.maintain insertion Ordered
2.Immutable after creation
3.Allow duplicate values
4.Can store heterogenious data
''')


tuple1 = ('12','13',)
print(tuple1)

tuple2 = tuple1+('14',)
print(tuple2)

tuple2 = tuple2+(str('Praneeth'),)
print(tuple2)

tupleWithoutParathesis = 1,2,3,4,5
print(tupleWithoutParathesis)

tupleWithSingleElement = (192,)
print(tupleWithSingleElement)

tupleConstructor = tuple([1,2,4])# Creating the tuple class object
print(tupleConstructor)


print()
t = (1,2,3,4,5,6,7)
print('negative indexing: ',t[-7])

print('Slicing',t[1:4])
print('indexing : ', t[3])



