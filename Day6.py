# OPP -> Concept/ideology to depict real-time scenario into programming language
# class --> A class is a user defined blueprint or prototype from which objects are created.
# It represents the set of properties or methods that are common to all objects of one type.
# In general, class declarations can include these components, in order:
# Modifiers: A class can be public or has default access (Refer this for details).
# class keyword: class keyword is used to create a class.
# Class name: The name should begin with an initial letter (capitalized by convention).
# class to create user defined data type
# object real time entity. Object: An Object is an identifiable entity
# with some characteristics and behaviour. An Object is an instance of a Class.
# When a class is defined, no memory is allocated but when it is instantiated
# (i.e. an object is created) memory is allocated.
# class contains variable , method collectively called properties/attributes

# Syntax
class NameOfClass:
    apple = 10
    juice = '50ml'


box1 = NameOfClass()
print(box1.apple)
print(NameOfClass.apple)

# variable inside class --> member variable , instance variable , class variable
# Methods inside class --> Methods --> class method --> instance(object) methods

# class with function/method


class Party2:

    def mix(self):
        print("hello juice")


box2 = Party2()
box2.mix()


class Access:
    num = 1

    def work(self):             # Dependent of class/member variables
        print(self.num)

    def test(self):             # Independent of class/member variables
        print("inside test")


ob = Access()
ob.work()
print("======================================================")


class Operations:

    def add(self, a, b):
        self.my_sum = a+b

    def mul(self, a, b, c):
        self.my_multi = a*b*c

    def disp_add(self):
        print(self.my_sum)

    def disp_mul(self):
        print(self.my_multi)


res = Operations()
res.add(10, 20)
res.mul(10, 20, 30)
res.disp_add()
res.disp_mul()


print("======================================================")


class NewClass:
    insta_var = 0

    def change_var(self):
        self.insta_var = 2
        return self.insta_var


obj_NewClass = NewClass()
print(obj_NewClass.change_var())
print(obj_NewClass.insta_var)


class Checking:

    def check(self, my_list):
        for i in my_list:
            if i > 20:
                print("greater")
            else:
                print("less")


obj = Checking()
obj.check([11, 22, 33])

