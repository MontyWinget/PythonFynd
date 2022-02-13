# no need to specify return-type of a function
# Default Function -> Zero parameters

def outer_function(param1, param2):
    outer_var = 0

    def inner_function():
        some_var = param1 - param2
        print(some_var)

    inner_function()
    print(outer_var)


print(outer_function(20, 10))


def function1():
    x = 2

    def function2(a):
        x = 6
        print(a+x)
    print(x)
    function2(3)


function1()

print("-----------------------------------------------------")


# def my_function(param):
#     num = 1
#     if num <= param:
#         return num + my_function(num + 1)


# print(my_function(5))

# functionDef(Parameters)
# functionCall(args)

# Functions
# Default Functions


def default_function():
    print("Hello World")


default_function()

# Para Functions


def para_function(num1, num2):
    print(num1 + num2)


para_function(10, 20)

# Return type vs display on console


def display():
    print("this is to display on console")


display()
print(display())


def return_function():
    return "returning string value"


print(return_function())

result1 = return_function()
print(result1 * 2)


# Python Function variations

def terminate(num1, num2):
    print("num1 is - ", num1)
    print("num2 is - ", num2)


terminate(1, 2)


def terminate2(num1, num2):
    print("num1 is - ", num1)
    print("num2 is - ", num2)


terminate2(num2=1, num1=2)

print("-----------------Setting default values in Parameters-------------------")
# Setting default values in Parameters


def terminate3(num1, num2=10):
    print("num1 is - ", num1)
    print("num2 is - ", num2)


terminate3(1)
terminate3(2, 40)


def terminate4(num1=50, num2=10):
    print("num1 is - ", num1)
    print("num2 is - ", num2)


terminate4()
terminate4(num2=100, num1=500)


def terminate5(*num1):      # no of args not known, (*) makes tuple
    list1 = list(num1)
    print(list1)
    print("num1 is - ", num1[0])
    print("List1 is - ", list1[0])


terminate5(1, 2, 3, 4, 5)
terminate5(10)

# ERROR
# def terminate6(*num1):
#     print("num1 is - ", num1)
#     # print("num2 is - ", num2)
#
#
# terminate6(num1=(10))


def terminate7(num1, *num2):
    print("num1 is - ", num1)
    print("num2 is - ", num2)


terminate7(1, 2, 3, 4, 5)


# Inner Function

def outer_function():
    print("Outer Function")

    def inner_function():
        print("Inner Function")
    inner_function()


outer_function()

# Access outer function property


def outer_function1():
    print("Outer Function")
    num = 100

    def inner_function():
        print("access outer function property num - ", num)
    inner_function()


outer_function1()


# Inner Function with para of outer function

def outer_function2(take_num_val):
    print("Outer Function")

    def inner_function():
        print("access outer function property num - ", take_num_val)
    inner_function()


outer_function2(99)

