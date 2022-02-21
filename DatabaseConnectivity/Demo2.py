import cx_Oracle
import os
os.environ["PATH"] = "Path of the oracle instant client file"

# Establish connection to the database
con = cx_Oracle.connect('hr','hr', 'localhost/pdborc1')

cur = con.cursor()

query1 = "insert into student values(102, 'JOHN')"
query2 = "update student set sname='xyz' where sid = 102"
query3 = "delete student where sid = 102"

cur.execute(query3)

cur.close()
con.commit() # use commit when need to add to database. No need commit to retrieve data
con.close()

print("Completed!!!")
