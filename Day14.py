# File Handling
# .txt, .dat
# File --> open, read, write, append (MODE)

# File
file1 = open("myfile.txt", "r")
print(file1)

for data in file1:
    print(data)

# ------------------------------------

print(file1.read())
print(file1.readline())
print(file1.readlines())

# -------------------------------------

print(file1.read(16))
print(file1.readline(2))
print(file1.readlines(10))

# -------------------------------------

file1 = open("myfile.txt", "w")
# file1.write("\nLine3")
# file1.writelines(["Line1\n", "Line2\n"])

# -------------------------------------

file1 = open("myfile.txt", "a")
# file1.write("\nLine3")
# file1.writelines(["Line4\n", "Line5\n"])

# -------------------------------------

file1 = open("myfile.txt", "r")
print(file1.read())
file1.close()
print(file1.read()) # Error

# -------------------------------------

with open("myfile.txt", "r") as file1:
    print(file1.read())

# -------------------------------------

with open("myfile.txt", "r") as file1:
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        print(e)

    print(file1.read())

# -------------------------------------

with open("myfile.txt", "r") as file1, open("myfile2.txt", "a") as file2:
    data_to_be_copied = file1.read()
    file2.write(data_to_be_copied)

# -------------------------------------

with open("myfile.txt", "r") as file1:
    print(file1.readline())
    print(file1.readline())
    print(file1.tell())
    file1.seek()
    print(file1.readline())

# -------------------------------------

li = [1, 2, 3, 4, 5]
f1 = open("myfile.txt", "w")
f1.write(str(li))

f1 = open("myfile.txt", "r")
print(type(f1.read()))

# -------------------------------------

import pickle

li = [1, 2, 3, 4, 5]
f1 = open("myfile.txt", "wb")
pickle.dump(li, f1)

# -------------------------------------

li = [1, 2, 3, 4, 5]
f1 = open("myfile.txt", "rb")
print(pickle.load(f1))

# -------------------------------------




