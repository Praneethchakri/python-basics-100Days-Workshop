def addition(x, y):
    result = x + y
    return result


print(addition(1, 3))


# Default param Methods
def multiply(x, y=6):
    mul = x * y
    return mul


print(multiply(4))

defaultValue_z = 10


def add(x, y=defaultValue_z):
    sumation = x + y
    print(sumation)


add(5)
defaultValue_z = 5

add(5)
