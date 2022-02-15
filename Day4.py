# Tuple     -> immutable, ()
# Methods   -> count, Index

# Tuple
my_tup1 = ()
print(my_tup1)
print(type(my_tup1))

my_tup2 = (11, 1.2, "Python")
print(my_tup2)

# Index
print(my_tup2[-1])
print(my_tup2[-1][0])

# 'tuple' object does not support item assignment
# my_tup2[0] = 50

# Methods
# print -> multi index present in one tuple
my_tup3 = (1, 2, 3, 4, 5)
print(my_tup3.count(4))

print(my_tup3.index(3))

# tuple inside list
tuple_inside_list = [(1, 2), (3, 4)]
print(tuple_inside_list)
print(type(tuple_inside_list))

print(tuple_inside_list[1][1])

# Type Error - tuple' object does not support item assignment
# list_inside_tuple[1][1] = 44

tuple_inside_list.pop()
print(tuple_inside_list)

# List inside tuple
list_inside_tuple = ([1, 2], [3, 4])
print(list_inside_tuple)
list_inside_tuple[0][1] = 22
print(list_inside_tuple)

# del list_inside_tuple[0]

# Paren. fpr Expression
tuple_with_single_object = (10)
print(tuple_with_single_object)

tuple_with_single_object2 = (10,)
print(tuple_with_single_object2)

# only Shallow Copy
tup1_one = (1, 2, 3, 4, 5)
tup1_two = tup1_one

print(tup1_one)
print(tup1_two)

# Concat creates new object internally
tup_result = tup1_one + tup1_two

print(tup_result)

print(id(tup_result))
print(id(tup1_one))
print(id(tup1_two))

# Slice
print(tup_result[0:4])

print("----------------------------------------------------------------------------")

# Dictionary
# Syntax -> {}
# {Key : value}
# Mutable -> Hybrid
# Data inside dict -> [key -> can be anything apart from mutable object]
#                   -> [value -> can be anything]

# Creation Ways

# Empty Disc
dic1 = {}
print(type(dic1))

dic2 = {1: 100}
print(dic2)

dic3 = {1: 10, 2: 20, "lang": "python", "favlang": "Dart", 1.1: 50}
print(dic3)

# Type Error: unhashable type 'list'
# dic4 = {[1,2,3] : 100}
# print(dic4)

dic5 = {(1, 2, 3): 50}
print(dic5)

# Duplication of key is allowed But overwrite
dic6 = {1: 100, 2: 200, 1: 300}
print(dic6)

# Multi value with one key
dic7 = {1: [11, 22, 33]}
print(dic7)

# sub dict in the form of value only
dic8 = {2: {10: 20}}
print(dic8)

# Access
print(dic2[1])
print(dic3["lang"])
print(dic5[(1, 2, 3)])
print(dic7[1])
print(dic7[1][0])
print(dic8[2])
print(dic8[2][10])

# key Value Methods

print(dic3.keys())
print(dic3.values())

# Methods
dic_Method = {1: 10, 2: 20, 3: 30}

# Update takes dictionary
dic_Method.update({4: 40})
print(dic_Method)

# Update via manual way
dic_Method[2] = 99
print(dic_Method)

# More Methods
# Unknown Pair
dic_Method.popitem()
print(dic_Method)

dic_Method.pop(1)
print(dic_Method)

del dic_Method[2]
print(dic_Method)

my_new_dic = dic_Method.copy()
print(my_new_dic)

print(id(my_new_dic))
print(id(dic_Method))

# Sets
# {}
# Mutable, indexing not available
# sets math operations --> union, intersection, difference, symmetric diff.
# Duplication allowed but will discard at run time
# we do not have supersets in reality
# hetro. data allowed
# Mutable objects aren't allowed

set_one = {}
print(type(set_one))

set_two = {1, 2, "python", (10, 20)}
print(type(set_two))
print(set_two)

# Mutable Inside set
# TypeError: unhashable type: 'list'
# set_three = {[1,23], "java"}


# TypeError: 'set' object is not subscript-able
# set_four = {1, 2, 3, 4, 5}
# set_four[0]


# Methods
set_five = {1, 2, 3, 4, 5}
set_five.add(10)
print(set_five)

set_five.remove(5)
print(set_five)

# Ordered or UnOrdered    --> INDEX
# SORTING not present
set_order = {2, 1, 4, 3, 8, 5}
print(set_order)

set_order2 = {2, 1, 3.14, 4, 3, "abc", 8, 5}
print(set_order2)

# Unknown value
set_order2.pop()
print(set_order2)

# Operations
set1 = {1, 2, 3}
set2 = {10, 2, 3}

# All these methods returns
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.difference(set2))
print(set2.difference(set1))

# updates called set
print(set1)
set1.intersection_update(set2)
print(set1)

# Methods and their Operators
# | pipe Operator  --> Union
# &   --> Intersection
# ^ cap Operator  --> symm. diff.
# -   --> diff.

set11 = {1, 2, 3}
set22 = {10, 2, 3}
set33 = {10, 20, 7}

print(set11 | set22)
print(set11 & set22)
print(set11 ^ set22)
print(set11 - set22)

print(set11.difference(set22) - set33)

# Operator Precedence
print((set22 | set33) - set11)
