class PythonClass:

    def __init__(self,name):
        self.name = name
        self.version =[]


    def __getitem__(self, i):
        return self.version[i]

    def __len__(self):
        return len(self.version)

    def __repr__(self):
        return f"<Python Version Details {self.version}>"


    def __str__(self):
        return f"Python Details {len(self.version)}"



pythonV1 = PythonClass("FirstVerstion")
pythonV1.version.append('1.0.0')
pythonV1.version.append('1.0.1')
pythonV1.version.append('1.0.2')

print(PythonClass.__repr__(pythonV1))

print(PythonClass.__str__(pythonV1))