def greet(name):
    print(f"Hello {name}")


def math_calculation(number):
    try:
        result = number / 10;
    except ZeroDivisionError:
        print("Cannot divided by Zero")
    else:
        print("Value of number " + str(result))
    finally:
        print("Executing Finally Block for Clean up the resources")


def array_Index_Out_of_BoundException(intArray,indexValue):
    try:
        value = intArray[indexValue]
        print(value)
    except IndexError:
        print("Element Doesn't Exist ")
    else:
        print(" Index Value" + str(value))
    finally:
        print("Usual Exection Value ")


if __name__ == "__main__":
    greet("Praneeth")
    math_calculation(10)
    numbersList = [100];
    array_Index_Out_of_BoundException(numbersList,1)
