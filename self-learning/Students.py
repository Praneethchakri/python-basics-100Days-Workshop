class Students:
    def __init__(self,name,address):
        self.name=name
        self.address = address

    def printStudent(self):
        return self.name+" <==> "+self.address


student1 = Students("Praneeth","Germany") #once the object creation is done , the very next method to process or assign values to parameter is dunderinitmethod

print(student1.printStudent())
print(Students.printStudent(student1))