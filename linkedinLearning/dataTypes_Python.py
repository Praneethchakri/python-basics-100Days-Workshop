# Basic Data Types in Python: Numbers, Strings, Booleans, Sequences(List,Tuple), Dictionaries
pythonInt = 5
pythonstring = "Praneeth-Developer"
pythonString1 = 'PythonLearner'
pythonBoolean = True
pythonList = [1, 34, 2.34, 'Praneeth']
pythonTuple = (1, 43, 23)
pythonDictionary = {1: 'Praneeth', 2: "Diguvapalem",
                    1: "Chakravarthi"}  # if we repeat the same key, value will be overridden

print("Dictionary ", pythonDictionary)
print("List", pythonList)
print("Int", pythonInt)
print("String", pythonstring)
print("String", pythonString1)
print("Boolean ", pythonBoolean)
print("Tuple", pythonTuple)

# re declaring to same variable with diff value

pythonInt = "Five"
print("Redeclared from Int to String ", pythonInt)

# sequence Type
print(pythonList[2])
print(pythonTuple[1])

# subset/Slice of Sequence/List or Tuple
# pythonList = [1, 34, 2.34, 'Praneeth']
print(pythonList[1:4])  # slicing the
print(pythonList[1:4:2])  # step value to skip while iterating .. here 2 is the step value

# we can use Slice to reverse the list or tuple of sequences
# syntax as Above eg: list[1:4:2], 2 is step value to skip
print(pythonList[::-1])
print(pythonTuple[::-1])

# dictionaries is key value based structure, Key always should be unique

print("Dictionaries to Get value with Key ", pythonDictionary[1])

print("String" + str(123))

def someFucntion():
    global pythonstring ## By adding the global we are  declaring this variable as Global variable
    pythonstring = "def" ## the changes we are doing here will affect(Override) the global value as well
    print(pythonstring)

someFucntion()
print(pythonstring)

del pythonstring ## deleting the defination of variable after declared/used , using del statement we can undefined the variables.
print(pythonstring) ## Error: NameError: name 'pythonstring' is not defined. Did you mean: 'pythonString1'?