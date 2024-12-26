

intType = 23
stringType = "Praneeth"
booleanType = True
floatType = 23.3

# sequence Types
listType = [1,12.2,'Diguvapalem',"Praneeth",True]

tupleType = (1,2,2.34,True,'Chakravarthi',"Praneeth")

dictionaryType = {"One" : 'Praneeth',"Two":"Chakravarthi","Three":"Diguvapalem"}


print(f"Integer:: {intType},\n StringType: {stringType} \n BooleanType: {booleanType},\n "
      f"floatingType :: {floatType}, "
      f"List Type {listType[0:2]} from index 0 to 2 only"
      f"List Type {listType[::-1]} reversing the List Data\n"
      f"List Type {listType[0:4:1]} step Fucntion to Skip the index 1 value \n"
      f"Tuple Type {tupleType[::-1]} Revesing the Tuple Data \n"
      f"Tuple Type {tupleType[0:6:2]} skip function/step Function the index 3 Value \n"
      f"Dictionary Type {dictionaryType['One']} Getting the index one value by passing key as One \n"
      f"Dictionary Type {dictionaryType['Two']} key Two ")


