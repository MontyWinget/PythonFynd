# # Multilevel Inheritance
# class GrandParent:
#     grand_parent_property = "grand parent property accessed"
#
#     def show_method_grandparent(self):
#         print("Inside Grand Parent Method")
#
#
# class Parent(GrandParent):
#     parent_property = "parent property  accessed"
#
#     def show_method_parent(self):
#         print("Inside Parent Method")
#
#
# class Child(Parent):
#     child_property = "child property  accessed"
#
#     def show_method_child(self):
#         print("Inside Child Method")
#
#
# ch = Child()
#
# print(ch.grand_parent_property)
# print(ch.parent_property)
# print(ch.child_property)
#
# ch.show_method_grandparent()
# ch.show_method_parent()
# ch.show_method_child()
#
# # Multiple Inheritance -> 2 parent 1 child
# # Example - 1
#
#
# class Parent1:
#     def parent1_method(self):
#         print("parent1_method")
#
#
# class Parent2:
#     def parent2_method(self):
#         print("parent2_method")
#
# class Child(Parent1, Parent2):
#     pass
#
#
# ch1 = Child()
# ch1.parent1_method()
# ch1.parent2_method()
#
# # Example 2
#
#
# class Parent11:
#     def parent_method(self):
#         print("parent11_method")
#
#
# class Parent22:
#     def parent_method(self):
#         print("parent22_method")
#
#
# class Child11(Parent11, Parent22):
#     pass
#
#
# ch11 = Child11()
# ch11.parent_method()
#
# # Hybrid Inheritance -> Grand Parent <- 2 Parents <- Child


# class GrandParent:
#     def grand_parent_method(self):
#         print("grand parent method")
#
#
# class Parent1(GrandParent):
#     def parent1_method(self):
#         print("parent1 method")
#
#
# class Parent2(GrandParent):
#     def parent2_method(self):
#         print("parent2 method")
#
#
# class Child(Parent1, Parent2):
#     def child_method(self):
#         print("child method")
#
#
# ch = Child()
# ch.grand_parent_method()
# ch.parent1_method()
# ch.parent2_method()
# ch.child_method()

# Hybrid Inheritance -> Diamond Problem Solved

class GrandParent:
    def show(self):
        print("show method, Grand parent class")


class Parent1(GrandParent):
    pass


class Parent2(GrandParent):
    pass


class Child(Parent1, Parent2):
    pass


ch = Child()
ch.show()









