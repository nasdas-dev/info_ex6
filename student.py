from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}


    def add_module(self,module):
        self.modules.append(module)
        self.grades[str(module)] = module.get_grade()

    def get_list_modules(self):
        print("Modules of Student " + self.name + ":")
        for module in self.modules:
            print(module)

    def get_grades(self):
        print("Grades of Student " + self.name + ":")
        for pairs in self.grades:
            print(str(pairs) + ": " + str(self.grades[pairs]))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
