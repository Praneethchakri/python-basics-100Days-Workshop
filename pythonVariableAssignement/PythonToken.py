print("Smallest Meaningful components is called PythonToken:::")
print("Keywords,Identifiers,Literals,Operators")

print("Keywords:: Some sort of reserved words, convey a special meaning to the compiler/interpreter ,Each keyword "
      "have a special meaning and specfic operation")
print("NEVER use it as a variable")
print("True, False,None,and,as,asset,def,class,continue,break,"
      "global,else,elif,finally,del,except,for ,if ,from,import,raise,try,or,return,pass,nonlocal,in,not,is ,lambda,"
      "")


print("Identifier")
print("Identifiers are the name used to identify a variable ,function,class,or an object")
print("RULES defined for naming an identifiers::")

print("Should not use the Reserver keywords"
      "should not use any special characters except '_'  and should not start with numbers. , Python varialbes as case sensitive, Var, var both considered different variables.")

_age= 33
print(f"{_age}")

#     123Age = 33
#       ^
# SyntaxError: invalid decimal literal

# 123Age = 33
# print(123Age)

print("Literals:: 4 Types,String,Numeric,Boolean,Special Literals")
print("STRING Literals: Both single and Double quotes are allowed ")
print("To Print multiple lines,  we use 3 single quotes to print ")
multiline = ''' String123
                  string2
                  String3'''
print(multiline)


print("NUMERIC Literals:: Int,Long,Float,Complex Literals")
print("Int +ve,-ve numbers with no fraction part, eg:101,-023")
print("Long :: Unlimited Integer size followed by Upper or lower l eg: 12313213L,2134232l")
print("Float:: -3.43")
print("Like in other programming languages, So limit for numeric variables to store with in certain range, "
      ",based on available memory and expand to the limit to store the value, No special arrangements to store the value.")

print("Boolean literals:: True,False")

print("Special Literals:  None,whcih is equal to null in other programming languages")
print("Used to specify the filed which that is not created ")

val1 = 10;
val2 = None
print(f"{val2} {val1}")



