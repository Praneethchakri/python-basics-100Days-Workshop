# prime number is a  number which is divisable by 1 or the number itself

# print(2 % 3 == 0)

for n in range(2, 10):
    for x in range(2,n):
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break
    else:
        print(f'{n} is prime number')
