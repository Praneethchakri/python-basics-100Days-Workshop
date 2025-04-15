print("Tuples Is a Data Structure in Python ")
print("Tuples are a group of values within ()")

tuple1 = (1,2,3,5,6,7)
tuple2 = ('a','b','c','d')

print(f"Tuple1 {tuple1}")
print(f"Tuple2 {tuple2}")
print("Operation to perform concatinations in Tuples")

tuple1 += tuple2
print(tuple1)

print("Indexing:: ")
print(tuple1[1])
print(tuple1[-1])

print("Slicing in Tuples:")
tuple1= tuple1[1:4]
print(tuple1)