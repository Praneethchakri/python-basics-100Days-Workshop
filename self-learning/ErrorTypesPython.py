# IndexError  friends =['test','test1'],
# friends[2] will cause IndexError
# KeyError: While accessing the key from dictionary if the value not found or missmatch
# NameError :
# AttributeError
# NotImplementedError :To Handle ongoing implementation to have user undestandable message
# RuntimeError
# SyntaxError
# IndentationError
# TabError
# TypeError
# ValueError
# ImportError:
# DeprecationWarning : DeprecationWarning bcoz of outdated features from library to show the warning while implementing


class Garage:

    def __init__(self):
        self.car=[]


    def __repr__(self):
        return f"{self} Details"


