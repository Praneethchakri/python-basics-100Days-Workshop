x = (20,)
print(type(x))

print(sum(x,10))

def printExactString(str):
    "Sample Fucntion to Print the data"
    print(str)
    return;


printExactString("Welcome to Python World  Dear Learner!!")
printExactString("Praneeth")


def mutableCheck (args):
    print("I/p ",id(args))
    args = args+(5,)
    print("After Increment ",id(args))
    return;

# var = 123
# var=[1,2,3,4]
var = (1,2,3,4) #Immutable, Global referance will not update
mutableCheck(var);
print("After Fucntion Execution",var)







