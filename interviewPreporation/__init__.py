def generator(n):
    i = 0;
    while i < n:
        yield i
        i += 1


# normal function
def normalFunction(n):
    result = []
    for i in range(n):
        result.append(i)
    return result


# if __name__ == '__main__':


gen = generator(5)  # returns gen as iterator
for number in gen:
    print(number)

num = normalFunction(10)
print(num)


def infiniteNumbers():
    num = 0
    while True:
        yield num
        num += 1
    return num


# infiNumber = infiniteNumbers()
# for number in infiNumber:
# print(number)


# Multiple Generatore pipline for data processing

def square_the_number(numbers):
    for number in numbers:
        yield number ** 2



def filter_even_number(numbers):
    for filterEven in numbers:
        if filterEven % 2 == 0:
            yield filterEven


i = range(10)
input_number = filter_even_number(square_the_number(i))
for i in input_number:
    print(i)

#List comprehension ,store all the values in Memory
square_Number = [i ** 2 for i in range(10)]
for x in square_Number:
    print(x)


square_Integer = (x ** 2 for x  in range(10))
for x in square_Integer:
    print(x)




