"""...................................
Programming paradigms are a strategy for reducing code complexity and determining the flow of execution. There are several different paradigms such as declarative, procedural, object-oriented, function, logic, event-driven, flow-driven more. These paradigms are not mutually exclusive.

.....................................
For example, Python is primarily object-oriented, but it's also procedural and functional. In simple terms, a paradigm can be defined as a style of writing a program.To help you understant OOP, I will first clarify some of it key components, which are classes, objects, and methods:

..................................
A CLASS is a logical code block that contains attributes and behaviour. In python, a class is defined with the class keyword. The attributes can be variables and the behaviour can be the function inside of it. In other words, a CLASS provides a blueprint for creating an object.

...................................
An OBJECT is an instance of a class and you can create any number of them. The state of an OBJECT comprises its attributes and behanvior, and each one has a unique identifier to distinguish it from other instances. The attributes and behaviour fo the class are what define the state of the object. For example, you can create the object EMP1 by calling the EMPLOYEE class; once called, you can define the position and employment status attributes as Shift Lead and Full-time respectively.

.....................................
Finally, there are METHODS which are the functions defined inside a class that determine the behavior of an object instance. Let's say you want the EMPLOYEE objects to output a string that states their position. You would first declare their function intro in the EMPLOYEE class and then call it on an object to get the outputs."""

# CONCEPTS OF OOP......................
"""INHERITTANCE, which is the creation of a new class by deriving from an existing one. The original class is called the PARENT or SUPERCLASS, or any derivatives are referred to as the SUBCLASS or CHILD CLASS.

 class Parent:
     Members of the parent class"""

"""class Child(Parent):
    Inherited members from parent class
    Additional members of the child class"""

"""POLYMORPHISM, It's a word that means having many forms. In the context of Python, polymorphism means that a single function can act differently depending on the object or the causes. For example, the (+) operator works differently for different datatypes. In the case of integer data types, the (+) operator performs addition operations such as 3 + 5 = 8. On the other hand, in the case of string datatype, the (+) operator performs a concatenation or combining two strings together. This ability of modifying functionality is called polymorphism.

string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)
output: polypolypoly 21 [1,2,3,1,2,3,1,2,3]"""

"""ENCAPSULATION, this means that Python can bind methods and variables from direct access by wrapping them within a single unit of scope, such as a class. Encapsulation helps prevent unwanted modifications, in effect, reducing the occurrence of errors and outputs.

class Alpha:

def __init__(self):
     self._a = 2.
     self.__b = 2.

self._a is a proteccted member and can be accessed by the class and its subclass
Private member can be accessed from the outside by using public methods to access them or by a practice known as "Name Mangling". example: _class__identifier (identifier is the data member that I want to access)"""


"""ABSTRACTION. This refers to the ability to hide implementation details to make data safer and more secure. Note that Python does not support abstraction directly and uses inheritance to achieve it.

from abc import ABC

class ClassName(ABC):
     pass
"""
