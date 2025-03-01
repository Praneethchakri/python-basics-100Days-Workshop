print("Even or Odd Number Finder:")


def evenOddFinder():
    number = int(input("Enter your Number :\n"))
    if number % 2 == 0:
        print(f"{number}  Is Even Number")
    else:
        print(f"{number}  is Odd Number ")


if __name__ == '__main__':
    evenOddFinder()
