"""
Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
"""


class School:
    # Define the class parameter "name"
    name = "Ecole"

    def __init__(self, name=None):
        # self.name is the instance parameter
        self.name = name

    def getname(self):
        return self.name


maisonneuve = School()
maisonneuve.name = "Maisonneuve"
print("%s name is %s" % (School.name, maisonneuve.name))

