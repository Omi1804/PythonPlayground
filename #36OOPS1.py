# OOP in Python

# To map with real-world scenarios, we started using objects in code.
# This is called object-oriented programming (OOP).

'''
For creating objects, we first create a class.
A class is a blueprint for creating objects.

Example:
'''

class Students:
    name = "Karan Kumar"

# Then we create an object from the class or an instance of the class
s1 = Students()
print(s1.name)  # Output: Karan Kumar

# Constructors
'''
All classes have a function called __init__(), which is always executed when the class is being initiated.
Constructors are invoked at the time of creation of objects.

If we don't create the init function ourselves, Python will create it for us under the hood.
'''

class NewStudents:
    name = "Karam"

    # The self variable refers to the instance of the class, similar to 'this' in other languages.
    # This self parameter is necessary to pass, otherwise, it will give an error.
    def __init__(self):
        print("Adding new students in DB")

s1 = NewStudents()  # The constructor will be executed automatically

# Parameterized constructor
class DynamicStudents:
    def __init__(self, fullname):
        self.name = fullname

s2 = DynamicStudents("OM Nigam")
print(s2.name)  # Output: OM Nigam

# The self parameter is a reference to the current instance of the class and is used to access variables that belong to the class.


# Classes are the collections of Attributes and methods

# Methods are the functions that belongs to the objects
# Methods also has self parameter necessary to pass, otherwise, it will give an error
# weather we use it or not


class Stud:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome to the python tutorials!!!", self.name)

    def get_marks(self):
        print("Your marks are : ", self.marks)

st = Stud("Om Nigam", 99)
st.welcome()
st.get_marks()