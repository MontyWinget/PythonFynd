# names = [("Ishan", "Kadam"), ("Prachi", "c")]
# str1, str2 = names
# list_1 = list(str1)
# list_2 = list(str2)
# print(list_1, list_2)

# arr1 = [2, 3, 6, 6, 5]                  # 5
# arr2 = [57, 57, -57, 57]                # -57
# arr3 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 6]   # 5
# arr4 = [6, 6, 6, 6, 6, 6, 6, 6, 6, 5]   # 5
# arr5 = [-7, -7, -7, -7, -6]             # -7
#
# arr = arr5
# arr.sort()
# maxItem = max(arr)
# for item in arr[::-1]:
#     if item < maxItem:
#         print(item)
#         break

# list1 = [1, 2, 3, 4, 5]
#
# def check(my_list):
#     for idx in range(len(my_list)):
#         if my_list[idx] % 2 == 0:
#             print("Number is Even")
#         else:
#             print("Number is Odd")
#
#
# check(list1)


def outer_func():
    x = 1

    def inner_func():
        x = 10
        print(x, "in inner Function")

    inner_func()
    print(x, "in outer Function")


outer_func()


class Sample:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.result = 0

    def divide(self):
        self.result = self.num1/self.num2

    def show(self):
        print(self.result)


obj1 = Sample(20, 10)
obj1.divide()
obj1.show()

# Day 7
# Question: Bank class with deposit and withdraw methods

class Bank:
    def __init__(self):
        self.current_bal = 2000

    def deposit(self, deposit_amt):
        self.current_bal = self.current_bal + deposit_amt
        print("Money added : ", deposit_amt, "Current Balance is :", self.current_bal)

    def withdraw(self, withdraw_amt):
        self.current_bal = self.current_bal - withdraw_amt
        print("Money withdrawn :", withdraw_amt, "Current Balance is :", self.current_bal)


obj = Bank()
obj.deposit(1000)
obj.withdraw(500)
obj.deposit(2000)


