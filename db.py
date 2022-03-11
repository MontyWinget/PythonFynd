import cx_Oracle

# Create a table in Oracle database
con = cx_Oracle.connect('hr/hr@localhost:1521/xe')
print(con.version)

# Now execute the sqlquery
cursor = con.cursor()

# cursor.execute("create table employee(empId integer, name varchar2(30), salary number(10, 2))")
# cursor.execute("insert into employee values(1, 'monty', 1000)")

cursor.execute("select * from employee")

# print(cursor)

for data in cursor:
    print(data)


# con.commit()


