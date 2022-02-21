import cx_Oracle
import os
os.environ["PATH"] = "Path of the oracle instant client file"

# Establish connection to the database
con = cx_Oracle.connect('hr','hr', 'localhost/pdborc1')

cur = con.cursor()

query = "select * from employees"

cur.execute(query)

for cols in cur:
    print(cols[0], "         ", cols[1],"         ", cols[2])


cur.close()

con.close()

print("Completed!!!")
