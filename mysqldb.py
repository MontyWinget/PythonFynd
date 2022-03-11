import mysql.connector

con = mysql.connector.connect(host='localhost', database='sample', user='root', password='123456')

cursor = con.cursor()

# creating table
# cursor.execute("create table employee1(emp_id integer, name varchar(10));")
# con.commit()

# adding values
cursor.execute("insert into employee1 values (1, 'test')")
cursor.execute("insert into employee1 values (2, 'test2')")
con.commit()

cursor.execute("select * from employee1")

for data in cursor:
    print(data)
