
# W292 no newline at end of file
# E225 missing whitespace around operator
# E265 block comment should start with '# '
# Use snake case instead of camel case naming convention
# Single Line Comment
# Dynamically typed language    -> No need to specify data types explicitly
# """ """  -> Used for multi line strings/comments

# Declaring Variables
num1 = 10
print(num1)
print(type(num1))
my_name = "Monty"
print(type(my_name))
print(my_name)
print("----------------------------------------------------------------")


# STRING TYPES
name = "Monty"  # Always suggested ""
lang = 'Python'
multi_line_string = '''Learning
Python'''
print(name)
print(lang)
print(multi_line_string)

print("----------------------------------------------------------------")


# INDEXING
print(name[0])
print(name[-1])
# IndexError: string index out of range
# print(name[8])
print("-------------------------------------------------------------------")

# SLICING / SUBS-STRING -> Property
# [start : end : step]
# start : Optional. An integer number specifying at which position to start the slicing. Default is 0
# end : Optional. An integer number specifying at which position to end the slicing. Default is n
# step : Optional. An integer number specifying the step of the slicing/Skipping. Default is 1
super_string = "my name is Python"
print(super_string)
print(super_string[0:1])
print(super_string[0:2])
print(super_string[0:3])
print(super_string[0:])
print(super_string[0:17])
print("----------------------------Slicing Start------------------------------------")
print(super_string[0::1])
print(super_string[0::2])
print(super_string[0::3])
print(super_string[::2])
print(super_string[::-1])
print(super_string[-1:-18:-1])
print(super_string[7:2:-1])
print("----------------------------Slicing End------------------------------------")

print("----------------------------Memory Allocation Start------------------------------------")
# STRING MEMORY ALLOCATION
name_of_lang = "Javaj"   # 3 object(J, a, v) -> passed into combined object
print(id(name_of_lang))
print(id(name_of_lang[0]))
print(id(name_of_lang[1]))
print(id(name_of_lang[2]))
print(id(name_of_lang[3]))
print(id(name_of_lang[4]))
# These are 6 different objects

print("----------------------Immutable Example------------------------------------------")

name_is = "Vipul"
print(id(name_is))
print(id(name_is.replace("V", "P")))
name_is = name_is.replace("V", "P")
print(name_is)
print(id(name_is))
print("----------------------------------------------------------------")


name = "Python"
other_name = name
print(id(name))
print(id(other_name))
other_name = "Cython"
print(id(name))
print(id(other_name))

print("----------------STRING METHODS---------------------------")
# EXAMPLE STRING METHODS
example = "This is a String"
example2 = "Ståle"
example3 = "sample"
print(example.endswith("e"))        # Returns true if the string ends with the specified value
print(example.title())              # Converts the first character of each word to upper case
print(example.swapcase())           # Swap cases lower case becomes upper case and vice versa
test_variable = example2.encode()
print(type(test_variable))    # Returns an encoded version of the string
print(type(example3))
print(example3.encode())
