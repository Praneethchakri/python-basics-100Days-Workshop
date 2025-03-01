import random
import customerModule

print("Random Module")
# Random Integer Value
print("random.random(x,y) ,x,y  is the range btw numbers, prints the random integer numbers")
random_Integer = random.randint(1, 100)
print(random_Integer)
# custome Module and import
print(customerModule.valueofPi)
# Random Floating Value
print("random.random()  prints the random float numbers")
random_float = random.random() * 10  # to print the number of range form 0-10 floating
print(random_float)

print("random.unifrom()  prints the random integer numbers,exclusion of range")
randomFloat = random.uniform(1, 10)
print(randomFloat)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
