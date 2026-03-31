class Person:
    def __init__(self,name,age):
        self.name = name
        self._age = age


    def __str__(self):
        return f"{self.name} of age {self._age}"

    @property # We can make a function to access as vairable using the @Property Decorator, the function should have only self variable in method
    def age(self):
        return self._age

p = Person("Praneeth", 34)
print(p.age)