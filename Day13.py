# Passing function as reference
# fun_name is --> ref variable

def fun_name():
    print("this is a function written somewhere")


print(id(fun_name))
print(type(fun_name))

fun_other = fun_name
fun_other()


def my_fun(fun_as_para):
    print("this is my_function")
    print(fun_as_para)
    fun_as_para()

my_fun(fun_name)


def outer(num):
    def inner_square():
        return num * num

    return inner_square

inner_logic = outer

print(inner_logic())


# Lambda function
my_lambda_fun = lambda num: num * num
print(my_lambda_fun(4))

my_lambda_fun2 = lambda num1, num2: num1 * num2
print(my_lambda_fun2(4, 5))

def outer():
    return lambda number: number * number

save_logic = outer()
print(save_logic(5))


def outer(num):
    return lambda inner_num: inner_logic * inner_logic

inner_logic = outer(10)
print(inner_logic(2))


def outer(num1, num2):
    return lambda inner_num: num1 * num2


call_inner_lambda = outer(10, 20)
print(call_inner_lambda(3))


# Decorators -> function
# it must take function as para
# it must have inner function   -> logic
# it must return inner function

def check_numbers(fun_as_para):
    def logic(num1, num2):
        if num1 < num2:
            num1, num2 = num2, num1
        return fun_as_para(num1, num2)
    return logic

# sub = check_numbers(sub)


@check_numbers
def sub(num1, num2):
    print(num1 - num2)


@check_numbers
def div(n1, n2):
    print(n1 / n2)


sub(10, 40)
div(2, 10)

# Question:
# def outer(num):
#     def inner_square():
#         return num * num
#
#     def inner_cube():
#         return num * num * num
#
#     return inner_square, inner_cube
#
#
# inner_square_logic, inner_cube_logic = outer(2)
# print(inner_cube_logic())
# print(inner_square_logic())


def outer(num):
    return lambda inner_num: inner_num * inner_num


inner_logic = outer(10)
print(inner_logic(20))














