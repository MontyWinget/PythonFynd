# MultiThreading

# MultiTask --> Paint, PyCharm
# Process  --> Paint
# Thread   --> unit process, light weight process

# Operating System --> PowerOn --> Thread -> BootUp
# BootUp -> BackGround Activities --> Threads (Daemon Thread)
# Program. --> MAIN THREAD  -->
# MAIN THREAD --> C LANG -> main() function
# MAIN THREAD --> c++, Java, c# -> main() Method

# Class --> Object => User Defined Thread

# 3 Ways to create Threads in python
# with function
# with class
# with class inheritance

# WAY1 -> with function

# from threading import Thread
#
# def my_thread_task():
#     print("this is user defined thread task")
#
#
# t1 = Thread(target=my_thread_task)
# t1.start()
#
# # WAY2 -> with class
#
# from threading import Thread
#
# class My_Simple_Class:
#     def my_thread_task(self):
#         print("this is user defined thread task")
#
#
# obj = My_Simple_Class()
# t1 = Thread(target=obj.my_thread_task())
# t1.start()


# WITH CLASS INHERITING THREAD CLASS
# example1-->
# from threading import Thread
#
# class My_Thread_Class(Thread):
#     def my_thread_task(self):
#         print("this is user defined thread task")
#
#
# obj = My_Thread_Class()
# obj.my_thread_task()  # --> Do Not Call Method Directly


# with class inheriting Thread class
# example2--->
# start() --> run()
# Both methods belongs to THREAD CLASS

# from threading import Thread
#
#
# class My_Thread_Class(Thread):
#     # Overriden Thread class run method
#     def run(self):
#         print("this is user defined thread task")
#
#
# obj = My_Thread_Class()
# obj.start()

# UDERSTANDING USER AND MAIN THREAD
# example1-->
# from threading import Thread
#
# class My_Thread_Class(Thread):
#     def run(self):
#         print("this is user defined thread task")
#
#
# th1 = My_Thread_Class()
# th1.start()
# print("this is main thread task")



# example2-->
# from threading import Thread
# class My_Thread_Class(Thread):
#     def run(self):
#         for num in range(1, 6):
#             print(num)
#
#
# th1 = My_Thread_Class()
# th1.start()
# for num in range(1, 6):
#     print(num)
# # MULTITHREADING TYPES --> SYNC, ASYNC
# # multi Threads --> 1 Source
#
#
# Example 1 -> ASYNC
#
# import threading
#
# list_of_dish = ["Biryani", "Paneer Tikka", "Aallo ke Parathe"]
#
# class Food:
#     def dish(self):
#         for dis_var in list_of_dish:
#             print(dis_var)
#
#
# class Person_One(threading.Thread):
#     def __init__(self, obj):
#         super().__init__()
#         self.obj = obj
#
#     def run(self):
#         self.obj.dish()
#
# class Person_two(threading.Thread):
#     def __init__(self, obj):
#         super().__init__()
#         self.obj = obj
#
#     def run(self):
#         self.obj.dish()
#
#
#
# f1 = Food()
#
# p1 = Person_One(f1)
# p2 = Person_two(f1)
#
# p1.start()
# p2.start()


# Example 2 -> SYNC
# import threading
#
# list_of_dish = ["Biryani", "Paneer Tikka", "Aallo ke Parathe"]
#
# class Food:
#     def dish(self):
#         lock.acquire()
#         for dis_var in list_of_dish:
#             print(threading.current_thread().name() + "-> " +dis_var)
#         lock.release()
#
# class Person_One(threading.Thread):
#     def __init__(self, obj):
#         super().__init__()
#         self.obj = obj
#
#     def run(self):
#         self.obj.dish()
#
# class Person_two(threading.Thread):
#     def __init__(self, obj):
#         super().__init__()
#         self.obj = obj
#
#     def run(self):
#         self.obj.dish()
#
#
# lock = threading.Lock()
# f1 = Food()
#
# p1 = Person_One(f1)
# p1.setName("person1")
#
# p2 = Person_two(f1)
# p2.setName("person2")
#
# p1.start()
# p2.start()

# # JOIN METHOD
# example1--
import threading

def my_thread_task():
    for num in range(1, 11):
        print(num)


t1 = threading.Thread(target=my_thread_task)
t2 = threading.Thread(target=my_thread_task)
t3 = threading.Thread(target=my_thread_task)

t1.start()
t1.join()
t2.start()
t3.start()

# # Sleep
# from threading import Thread
# from time import sleep
#
# def my_thread_task():
#     for num in range(1,6):
#         sleep(4)
#         print(num)
#
#
# t1 = Thread(target=my_thread_task)
# t1.start()
#
# # THREAD DISPATCHER     -> HANDLES THREAD
# # THREAD SCH            -> DECIDES TIME THREAD      --> SFJ, ROUND ROBIN, FIFO, LIFO
#
#
#
# MyThread m1 = new MyThread();
#
#
#
#
#
#
# # QUESTION1 -->
# # CONSUMER -> PRODUCER PROBLEM
