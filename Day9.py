# Feb 15, 2022


# ---------------- ENCAPSULATION -------------------
# Wrapping of data
# Box(class) --> 10 things(data and methods) --> pack kardo
# Makes your data secure and accessible
# Access modifier (specifiers) - public, protected, private
# 1. public    --> full access (by default)
# 2. protected --> _ - single underscore before v_name, outside class + child class + within package
# 3. private   --> __ - double underscore, within class only

class Check_Access_Specifier:
    num = 100  # public
    _name = "Python"  # protected
    __id = 10.19  # private

    def access_private_fields(self):
        print(self.__id)


object = Check_Access_Specifier()
print(object.num)  # prints 100
print(object._name)  # prints Python
# print(object.__id)    # Will give an error

object.access_private_fields()  # will print 10.19 because access method is public


# ---------------------------------------------------------

class Change_Access_Specifier:
    __id = 10.19  # private

    def change_private_fields(self):  # this is called write access
        self.__id = 10

    def display_private_memebers(self):  # this is called read access
        print(self.__id)


object = Change_Access_Specifier()
object.change_private_fields()
object.display_private_memebers()  # will print 10


# ----------2 ways to initialise objects-------------------

# 1. Constructor or init for python
# 2. Using getter and setter methods -> better use is to change private fields + for validation purpose

class Check_Access_Specifier:
    def __init__(self):  # init is public by default, you cannot make this private.
        print("Object Created")


Check_Access_Specifier()  # prints Object Created


# ---------------------------------------------------------

class Check_Access_Specifier:
    def __init__(self):
        self.__name = None
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def display(self):
        print("Name:", self.get_name())  # prints Python
        print("Age:", self.get_age())


obj1 = Check_Access_Specifier()
# print(obj1.__name)                  # Error because name is private

obj1.display()  # prints 0 and None (defaults)

obj1.set_name("Python")
obj1.set_age(30)

print("Name:", obj1.get_name())  # prints Python
print("Age:", obj1.get_age())  # prints 30

# ---------------- QUESTION----------------------------------
# Validate user input, A person must have 2 details to take admission in FYND
# 1. age > 20
# 2. name = check blank spaces
# then init the person with 2 details if validated else provide default values

class Validate:

    def __init__(self):
        self.__name = "NewUser"
        self.__age = 0

    def set_name(self, name):
        if name.isspace() == False:
            self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age > 20:
            self.__age = age

    def get_age(self):
        return self.__age

    def details(self):
        print("Name of user:", self.__name)
        print("Age of user:", self.__age)


person = Validate()

person.get_name()  # will print default values
person.get_age()

person.set_name("XYZ")
person.set_age(19)

person.get_name()  # prints XYZ
person.get_age()  # prints 0

person.set_age(35)
person.details()  # prints XYZ and 35


# strings = " Y "
# print("Answer of is space:",strings.isspace())      # check this please
# ---------------------------------------------------------

# ---------------- ENCAPSULATION WITH INHERITANCE ------------------------------
class Parent:
    __private_num = 7
    _protected_name = "Python"

    def show(self):
        print(self.__private_num)


class Child(Parent):
    def display(self):
        super().show()


obj = Child()
# print(obj.__private_num)            # Error
obj.display()  # prints 7
print(obj._protected_name)  # prints Python

# ---------------- IMPORT WAYS ------------------------------
# Also refer day9(import).py

# File 1

# num = 10

# def show():
#     print("Hello World")


# # File 2
# import File1

# print(File1.num)               # Bottleneck - imports entire contents of file 1


# File 1

# num = 10

# def show():
#     print("Hello World")


# # File 2
# from File1 import num

# print(num)               # better import
# ---------------------------------------------------------


# File 1

# num = 10

# def show():
#     print("Hello World")


# # File 2
# from File1 import show as show_function

# print(show_function())
# ---------------------------------------------------------


# ---------------- ABSTRACTION -------------------
# Hiding of Data + Providing access

# eg: Laptop internals (hidden) + using laptop (providing access)

# Rules:
# 1. abstract class -->
#   a. No object creation possible
#   b. abstract method only in abstract class
#   c. can also contain simple methods and variables
# 2. abstract method means only method declaration
# 3. direct abstraction is not possible in python
# 4. you can inherit abstract class

# compulsory
from abc import ABC, abstractmethod


# from abstract class package, abstract the abstract class


# Incomplete abstract class
class Abstract_Class(ABC):
    pass


obj = Abstract_Class()  # should give error but python doesn't throw one because it's an incomplete abstract class


# --------------------------------------------------------------------

# Complete abstract class
class Abstract_Class(ABC):

    @abstractmethod
    def abstract_method(self):  # not technically an abstract method because it has implementation
        print("Hello")


# obj = Abstract_Class()          # will now give error

# --------------------------------------------------------------------

# Proper abstract class and it's implementation
class Abstract_Class(ABC):
    @abstractmethod
    def abstract_method(self):  # proper abstract method
        pass


class Implementation(Abstract_Class):
    # to avoid making this an abstract class as well, override the abstract method
    def abstract_method(self):
        print("Implementation of abstract class")


obj = Implementation()
obj.abstract_method()


# --------------------------------------------------------------------

# Abstract class with multiple methods
class Abstract_Class(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def simple_method(self):
        print("Method with body i.e. not an abstract method")

    def __init__(self, age):
        print("init in abstract class")  # valid and will print when object of inherited class is created
        self.age = age


class Implementation(Abstract_Class):

    def __init__(self):
        super().__init__(27)

    # to avoid making this an abstract class as well, override the abstract method
    def abstract_method(self):
        print("Implementation of abstract class")


obj = Implementation()
obj.abstract_method()  # Prints Implementation of abstract class
obj.simple_method()  # prints Method with body i.e. not an abstract method
print(obj.age)  # Prints 27




