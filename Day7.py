# class Numbers:
#     def instance_method(self):
#         print("This is instance method")
#
#
# ref_var = Numbers()
# print(id(ref_var))
# ref_var.instance_method()
# Numbers.instance_method(ref_var)

print("------------------------------------------------------")


class Numbers1:
    my_num_val = 100

    def instace_method1(self, my_num_val):
        print(my_num_val)


ref_var1 = Numbers1()
ref_var1.instace_method1(50)
print(ref_var1.my_num_val)


print("------------------------------------------------------")


class Numbers2:
    my_num_val = 100

    def instance_method2(self, my_num_val):
        print(self.my_num_val)
        print(my_num_val)


ref_var2 = Numbers2
ref_var2.instance_method2(50)
print(ref_var2.my_num_val)

print("------------------------------------------------------")


class Numbers3:
    my_num_val3 = 100

    def instance_method3(self, my_num_val3):
        self.my_num_val3 = my_num_val3


ref_var3 = Numbers3
ref_var3.instance_method3(50)
print(ref_var3.my_num_val3)


print("------------------------------------------------------")

# Method Definition     --> my_num = 50
# Method Declaration    --> my_num;

# Question:
# class Numbers:
#     pass
#
#
# ref_var = Numbers()
# ref_var.my_num_val = 100
# print(ref_var.my_num_val)
#
# ref_var2 = Numbers()
# print(ref_var2.my_num_val)

# -----------------------INIT METHOD------------------

# init  --> auto invoked
# init  --> will get called sep for each object
# init  --> it is a special method to initialize object
# init the object   --> passing value to properties for specific object.

# Example 1


class Numbers4:
    def __init__(self, take_val):
        num = take_val
        print(num)


obj = Numbers4(50)
print(obj.num)

# Example 2     --> using self


class Numbers5:
    def __init__(self, take_val):
        self.num = take_val
        print(self.num)


obj1 = Numbers5(100)
obj2 = Numbers5(200)
print(obj1.num)
print(obj2.num)

# What actually init is


class Numbers6:
    def __init__(self):
        print("inti is getting called")
        print("i am not a constructor")


my_obj = Numbers6()
Numbers6.__init__(my_obj)
my_obj.__init__()


class Sample:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def show(self):
        print(self.num1)
        print(self.num2)
        print(self.num3)


obj1 = Sample(10, 20, 30)
obj1.show()

obj2 = Sample(100, 200, 300)
obj2.show()




