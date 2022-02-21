import cx_Oracle
import os
os.environ['PATH'] = 'Path of the oracle instant client file'

# Establish connection to the database

con = cx_Oracle.connect("username","password", "localhost/pdborc1")

print("Connected!!!!")

con.close()