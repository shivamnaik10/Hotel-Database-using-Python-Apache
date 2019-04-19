#!C:/Rutgers/Sem 1/BDM/Project/BDM project/venv/Scripts/python.exe
print("Content-Type: text/html")
print()
import cgi,cgitb
import codecs
cgitb.enable() #for debugging
form1 = cgi.FieldStorage()
email = form1.getvalue('email')
name = form1.getvalue('name')
Phone = form1.getvalue('phone')


f=codecs.open("form2.html", 'r')
print(f.read())

import pymysql

# Open connection to the database
db = pymysql.connect("localhost","root","root123","bdmproject", autocommit=True)

# Start a cursor object using cursor() method
cursor = db.cursor()

#Create query
sql = """INSERT INTO CUSTOMERS(name, email, cell_no) VALUES(%s, %s, %s);"""

# Execute a SQL query using execute() method.
cursor.execute(sql,(name, email, Phone))
cursor.execute("commit")

# Fetch all the rows using fetchall() method.
#data = cursor.fetchall()
#print (data)

# disconnect from server
db.close()