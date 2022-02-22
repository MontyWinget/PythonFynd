# Polymorphism
# Method Overloading
# Operator Overloading
# Method Overriding
# Duck Typing

# ----------Method Overloading----------
# Atleast 1 class
# 2 methods (same name, same count of parameters with different data types)
#           (same name,  diff count of parameters with same or different data types)

# Example 1
# class MyOverloading:
#     def method_one(self, num1 , num2):
#         print("Overload 1")
#
#     def method_one(self, num):
#         print("Overload 2")
#
#
# obj = MyOverloading()
# obj.method_one(10)

# Method Overriding
# Atleast 2 classes having inheritance relationship
# Each having same method name with same signature


# class Parent:
#     def info(self, blood, surname):
#         print(blood, surname)
#
#
# class Child:
#     def info(self, blood, surname):
#         print(blood, surname)
#         print("this is child class additional method")
#
#
# ch = Child()
# ch.info("A+", "surnameIS")

# class Parent:
#     def info(self, blood):
#         print(blood)
#
#
# class Child:
#     def info(self, blood, surname):
#         print(blood, surname)
#         print("this is child class additional method")
#
#
# ch = Child()
# ch.info("A+")

# How to print Object
# def __str__(self): --> only returns string

# class Demo:
#     def __init__(self, num):
#         self.num = num
#
#     def __str__(self):
#         return str(self.num)
#
#
# obj = Demo(7)
# obj2 = Demo(10)
#
# print(obj)
# print(obj2)

# Operator overloading

# class Demo:
#     def __init__(self, num):
#         self.num = num
#
#     def __str__(self):
#         return str(self.num)
#
#     def __add__(self, other):
#         return self.num + other.num
#
#     def __gt__(self, other):
#         return self.num > other.num
#
#
# obj = Demo(7)
# obj2 = Demo(10)
#
# print(obj + obj2)
# print(obj2 > obj2)


# Question : override operator methods for more than 2 objects

class Demo:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return Demo(self.num + other.num)

    def __gt__(self, other):
        return self.num > other.num


obj = Demo(7)
obj2 = Demo(10)
obj3 = Demo(10)
obj4 = Demo(10)
x = obj + obj2 + obj3
print(x)

# Question1 -> validate user input, A person must have 2 details to take admission in FYND
#               1. age > 20
#               2. check blank spaces
# Than init  the person with 2 details if validated else provide default values

class Admit:
    def __init__(self):
        self.__age = 0
        self.__name = None

    def set_age(self, age):
        if age > 20:
            self.__age = age

    def set_name(self, name):
        if not name.__contains__(" "):
            self.__name = name

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name


person1 = Admit()
person1.set_age(23)
person1.set_name("monty")

print(person1.get_name())
print(person1.get_age())





