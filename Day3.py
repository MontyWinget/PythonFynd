# List
li1 = []
print(li1)
print(type(li1))

# Any type of elements can be added
li2 = [1, 2, 3, 4, 5]
print(li2)

li3 = [1, 1, 5, "Python"]
print(li3)
print(li3[3])

# Mutable
my_list = [1, 2, 3, 4, 5]
print(my_list[0])

my_list[2] = 33
print(my_list)

# Slicing
print(my_list[::-1])

# Passing Reference - Shallow Copy
print("Shallow Copy Example")
other_list = [11, 22, 33, 44, 55]
new_list = other_list
print(other_list)
print(new_list)
print("After Modification")
new_list[2] = 90
print(other_list)
print(new_list)
print(id(other_list))
print(id(new_list))

print("_____________________________________________________")
# Passing Object - Deep Copy
print("Deep Copy Example")
other_list2 = [11, 22, 33, 44, 55]
new_list2 = other_list2.copy()
print(other_list2)
print(new_list2)
print("After Modification")
new_list2[2] = 90
print(other_list2)
print(new_list2)
print(id(other_list2))
print(id(new_list2))

print("_____________________________________________________")
# Methods --> Adding
# 3 ways for adding methods
# Insert    -> returns none
# Append    -> returns none
# Extend    -> returns none,    accepts only iterables

print("Methods for adding")
my_obj_list = [1, 2, 3, 4, 5]
print(my_obj_list)

my_obj_list.insert(0, "Java")
print(my_obj_list)

my_obj_list.append("20.15")
print(my_obj_list)

# my_obj_list.extend(50)
# 'int' object is not iterable

print(my_obj_list.extend([[11, 22], [33, 44]]))
print(my_obj_list)

print("_____________________ Remove Examples ________________________________")
# Methods --> Remove
print("Methods for Remove")
print(my_obj_list)

# pop -> 2 variations,  -> both returns the value which is removed
# pop with index
# pop without index

print(my_obj_list.pop())
print(my_obj_list)

print(my_obj_list.pop(0))
print(my_obj_list)

# Remove -> Takes parameter as the value to remove, returns none
my_obj_list.remove(3)
print(my_obj_list)

print("___________________Remove All Data__________________________________")
# Remove all data
my_obj_list.clear()
print(my_obj_list)
print(id(my_obj_list))

# del -> keyword
del my_obj_list
# print(my_obj_list) -> name 'my_obj_list' is not defined

print("_____________________________________________________")
list1 = [1, 2, 3]
del list1[0]
print(list1)

# pop vs del
print(list1.pop())
print(list1)

list2 = [1, 2, 3, 4, 5, 5, 5]
print(list2.count(5))

# print(list2.append(6))      --> none

print(list2.append(6))
print(list2)

# List
print("-----------List Comprehension-------------")

my_items = []
for add_items in range(1, 5):
    my_items.append(add_items)

print(my_items)

my_items_list = [add_elements for add_elements in range(1, 6)]
print(my_items_list)

my_items_list2 = [elements * elements for elements in range(1, 5)]
print(my_items_list2)

# list within list
print("---------------List within List -----------------------")

sub_list = [33, 44, 55]
super_list = [1, 2, sub_list]
print(super_list)

print(super_list[2])
print(super_list[2][1])

# multi loop with list
print("multi loop with list")
super_list2 = [[1, 2], [11, 22]]
empty_multi_list = []
for dimOne in super_list2:
    for data in dimOne:
        empty_multi_list.append(data)

print(empty_multi_list)

super_list2_new = [[31, 32], [41, 42]]
empty_multi_list_new = [data_new for dimOne_new in super_list2_new for data_new in dimOne_new]
print(empty_multi_list_new)


# ZIP Function
print("-------------------------- Zip Function ---------------------")

print("First Approach")
my_list_one = [1, 2, 3, 4, 5]
my_list_two = [11, 22, 33, 44, 55]
my_zip_created_list = []

for elements in my_list_one, my_list_two:
    my_zip_created_list.append(elements)

print(my_zip_created_list)


print("Second Approach")
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [11, 22, 33, 44, 55]
my_zip_created_list_other = []

for elements_new1 in zip(my_list_1, my_list_2):
    my_zip_created_list_other.append(elements_new1)

print(my_zip_created_list_other)

print("Third Approach")
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [11, 22, 33, 44, 55]
my_zip_created_list_other = []

print("---------------------------Zippppppppppppppp")
for elements_new1, elements_new2 in zip(my_list_1, my_list_2):
    print(elements_new1, elements_new2)

another_list = list[]

print("Fourth Approach")
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [11, 22, 33, 44, 55]
for elements_new1, elements_new2 in zip(my_list_1, my_list_2):
    print(elements_new1, elements_new2)

my_zip_created_list_other = [(elements_new1, elements_new2) for elements_new1, elements_new2 in zip(my_list_1, my_list_2)]
print(my_zip_created_list_other)













