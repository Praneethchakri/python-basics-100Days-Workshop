
def average(a,b,c):
    d = ( a + b + c )/3
    print(d)
    # return ( a + b + c )/3


r1 = average(5,5,8)
r2 = average(6,8,9)


print(r1)
print(r2)

# positional Arguments, we can pass in any order but the paramter should match the argument

def sum1(a,b):
    summ1  = a+b
    return summ1

# Default arguments are optional, need to be keep at the end

def sum(a,b,sample = 1): #Sample is a default value
    summ = a+b+sample
    return summ

print(sum1(b=5,a=3)) # keyword arguments should matche in short,
# we have given the position here to match a,b,with same name ,, and if we pass x=5,y=3 , it fails as the name missmatches
print(sum(6,8,2))



