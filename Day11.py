# Example1
# class -> ZeroDivisionError: message -> division by zero
print("Line1")
print("Line2")
print(50 / 0)      # Exception -> Terminate
print("Line4")
print("Line5")




# Example2
print("Line1")
print("Line2")
try:
    print(50 / 0)
except:
    print("please dont use 0 for division")

print("Line4")
print("Line5")



# Example3
# e is ref variable for object of Exception class which is created in HEAP MEMORY of RAM
print("Line1")
print("Line2")
try:
    print(50 / 0)

except Exception as e:
    print(e)

print("Line4")
print("Line5")



# Example4
print("Line1")
print("Line2")

num1 = 10
num2 = 0

try:
    print(num1 / num2)

except Exception as e:
    num2 = 2
    print(num1 / num2)

print("Line4")
print("Line5")





# Example5
# SPECIFIC EXCEPTION CLASS
print("Line1")
print("Line2")

try:
    list1 = [1, 2, 3]
    print(list1[10])

except IndexError as e:
    print(e)

print("Line4")
print("Line5")


# Example6
# MULTI EXCEPT BLOCKS
print("Line1")
print("Line2")
list1 = [1, 2, 3]

try:
    print(10 / 0)
    print(list1[10])

except IndexError as e:
    print("Block 1")

except ZeroDivisionError as e:
    print("Block 2")

print("Line4")
print("Line5")





# Example7
# TWO CLASSES HAVING SAME =EXCEPTIONS
print("Line1")
print("Line2")

try:
    print(10 / 0)

except ZeroDivisionError as e:
    print("Block 1")

except Exception as e:
    print("Block 2")

print("Line4")
print("Line5")

# Example9
# SPECIFIC TO GENERIC EXCEPTION CLASSES ONLY
# DO NOT TRY THIS AT HOME OR AT OFFICE
print("Line1")
print("Line2")

try:
    print(10 / 0)

except Exception as e:
    print("Blsock 2")

except ZeroDivisionError as e:
    print("Block 1")

print("Line4")
print("Line5")

# Example10
# Nested Exceptions
print("Line1")
print("Line2")

try:
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        print("Inner Block")

except Exception as e:
    print("Outer Block")

print("Line4")
print("Line5")


# Example11
# Nested Exceptions
print("Line1")
print("Line2")

try:
    print(10 + "10")
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        print("Inner Block")

except Exception as e:
    print("Outer Block")

print("Line4")
print("Line5")




# Example12
# Nested Exceptions
print("Line1")
print("Line2")

try:
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        print("Inner Block")
        print(10 / 0)

except Exception as e:
    print("Outer Block")

print("Line4")
print("Line5")


FINALLY BLOCK  --> GETS EXCECUTED EVERYTIME

# finally block atmost 1 time

1. try -> except -> finally
2. try -> finally


# Example1
# FINALLY BLOCK with except having exception
print("Start")

try:
    print(10 / 0)

except Exception as e:
    print(e)

finally:
    print("Finally Block")

print("End")

# Example2
# FINALLY BLOCK with except having NO exception
print("Start")

try:
    print(10 / 5)

except Exception as e:
    print(e)

finally:
    print("Finally Block")

print("End")

# Example3
# FINALLY BLOCK without except having exception
print("Start")

try:
    print(10 / 0)

finally:
    print("Finally Block")

print("End")




# Example4
# FINALLY BLOCK without except having No exception
print("Start")

try:
    print(10 / 3)

finally:
    print("Finally Block")

print("End")


# REAL TIME SCE FOR FINALLY BLOCK
try:
    print("Start")
    print("File Open")
    print("File Read / Write")
    print(100 / 0)

except Exception as e:
    print(100 / 0)
    print(e)

finally:
    print("File Close")


# RAISE Exception
# raise keyword only with EXCEPTION CLASSES
# raise create object of EXCEPTION CLASSES
marks = 10

if marks < 70:
    raise Exception("try again")
#    print("Documentation Process")     <-- This code is unreachable

else:
    print("welcome to company")
    print("Documentation Process")

# CUSTOME EXCEPTION
class NotSelectedException(BaseException):
    def __init__(self, msg):
        self.msg = msg
        print(self.msg)

marks = 10

if marks < 70:
    raise NotSelectedException("try again")

else:
    print("welcome to company")
    print("Documentation Process")

# CUSTOME EXCEPTION

class NotSelectedException(BaseException):
    def __init__(self, msg):
        super().__init__(msg)

marks = 10

if marks < 70:
    raise NotSelectedException("try again")

else:
    print("welcome to company")
    print("Documentation Process")

