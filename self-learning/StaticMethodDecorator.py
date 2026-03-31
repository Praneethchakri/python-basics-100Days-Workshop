class Student:
    def __init__(self,marks):
        self.marks = marks

    # def __str__(self):
    #     return f'{self.name} is located in {self.address}'

    def __repr__(self):
        return f'StudentMarks ::{self.marks}'

    @staticmethod
    def sumStdMarks(subj1, subj2):
        return Student(subj1 + subj2)


# stdObject   =  Student("Praneeth","Germany")
stdObject1 = Student.sumStdMarks(99,100)

print(stdObject1)