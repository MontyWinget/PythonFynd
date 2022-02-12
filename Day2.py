# CONTROL STATEMENTS
# if else
# use 4 spaces for indentation
# Simplify chained comparison
# Remove redundant parentheses

num1 = 10
num2 = 20
num3 = 30
# SINGLE IF
if num1 < num2 < num3:
    print("true")


# IF ELSE

if num1 > num3:
    print("True")
else:
    print("False")

# MULTIPLE CHECKS -> ELIF
if num1 == 20:
    print("True")
elif num2 == 20:
    print("num2 is 20")
else:
    print("nothing")

# Nested if else statements
name = "java"
if name == "vaja":
    print("it is java")

    if name == "cpp":
        print("we cpp found")
    elif name == "python":
        print("we found nothing")
    else:
        print("we are in the else")
else:
    print("Something else")


# For Loop
string_values = "Python"
for char in string_values:
    print(char)

# not in, in (membership operators)
print("y" in "python")
print("y" not in "python")

# range(start, stop, step)
print("-------------------Range Example-------------------")
for values in range(0, 10):
    print(values)

stored_numbers = range(10, 16)      # Type of variable will be class 'range'
print(type(stored_numbers))
print(stored_numbers)
for values in stored_numbers:
    print(values)

print("--------------------------------------------------------")
# While Loop
number = 1

while number < 10:
    print(number)
    number += 1

number2 = 20
while number2 < 25:
    print(number2)
    number2 += 1
    break                   # Breaks the loop and moves out

# for with else using break
print("--------------------For with else using break example------------------------------------")
for val in range(1, 11):
    if val < 12:
        print(val)
    else:
        break

else:
    print("number not found")

print("end line")

# While with else using break
value = 6
while value < 10:
    print(value)
    value += 1
    break
else:
    print("Else part of while")

print("--------------------------------------------------------------")


# Do while
sample_number = 10
while True:
    print(sample_number)
    sample_number += 1
    if sample_number > 10:
        break

print("---------------------------------------------------")
# Switch Case
some_number = 1
while True:
    if some_number == 1:
        print("one")
        break
    elif some_number == 2:
        print("two")
        break
    elif some_number == 3:
        print("three")
        break
    elif some_number == 4:
        print("four")
        break
    elif some_number == 5:
        print("Five")
        break
