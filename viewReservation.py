#!C:/Rutgers/Sem 1/BDM/Project/BDM project/venv/Scripts/python.exe
print("Content-Type: text/html")
print()

import cgi
import pymysql
form4 = cgi.FieldStorage()
cell_no =form4.getvalue('cell_no')


# Open connection to the database
db = pymysql.connect("localhost","root","root123","bdmproject", autocommit = True)

# Start a cursor object using cursor() method
cursor = db.cursor()

room_query = "select * from customers c,reservation r where c.cell_no = r.cell_no and c.cell_no = %s";

cursor.execute(room_query,(cell_no))
data = cursor.fetchall()
attribute_names = [i[0] for i in cursor.description]
print("<p>Room Details</p>")
print("<style>table { font-family: arial, sans-serif; border-collapse: collapse; width: 100%; } td, th { border: 1px solid #dddddd; text-align: left; padding: 8px; } tr:nth-child(even) { background-color: #dddddd; } </style>")
print("<table><tr>")

for columns in attribute_names:
    print("<th>",columns,"</th>")
print ("</tr>")

for rows in data:
    print ("<tr>")
    for subrows in rows:
        print("<td>",subrows,"</td>")
    print ("</tr>")
print("</table>")

# Get the number of rows in the resultset

db.close()