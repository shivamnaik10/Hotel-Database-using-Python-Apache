#!C:\Rutgers\Practice Workspace\Python Workspace pycharm\venv\Scripts\python.exe
print("Content-Type: text/html")
print()

import cgi
import cgitb
import pymysql
cgitb.enable() #for debugging
form = cgi.FieldStorage()
name = form.getvalue('fname')
print("Name of the user is:",name)



# Open connection to the database
db = pymysql.connect("localhost","root","root123","shivam")

# Start a cursor object using cursor() method
cursor = db.cursor()

# Execute a SQL query using execute() method. This should return all the columns of heroes that use swords.
cursor.execute(name)

# Fetch all the rows using fetchall() method.
data = cursor.fetchall()
print (data)

# disconnect from server
db.close()