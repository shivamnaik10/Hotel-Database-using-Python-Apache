#!C:/Rutgers/Sem 1/BDM/Project/BDM project/venv/Scripts/python.exe
print("Content-Type: text/html")
print()
import cgi,cgitb
import codecs
import pymsgbox
cgitb.enable() #for debugging
form2 = cgi.FieldStorage()
arrive = form2.getvalue('arrive')
depart = form2.getvalue('depart')
person = form2.getvalue('person')
roomtype = form2.getvalue('room_type')
roomnumber = form2.getvalue('room_number')
cellno = form2.getvalue('phone')


import pymysql

# Open connection to the database
db = pymysql.connect("localhost","root","root123","bdmproject", autocommit = True)

# Start a cursor object using cursor() method
cursor = db.cursor()

# Execute a SQL query using execute() method.

rows = cursor.execute("select * from reservation where room_type= '"+roomtype+"' and checkoutdate='"+depart+"'");

# Fetch all the rows using fetchall() method.
result = cursor.fetchall();
if len(result)!=0:
    print(
        '''<script>
        alert('Room not available ');
        </script>''')
    g = codecs.open("form2.html", 'r')
    print(g.read())

else:
    sql = "insert into reservation(arrivaldate,checkoutdate,noofperson,room_type,roomnumber,cell_no) values(%s,%s,%s,%s,%s,%s)";
    cursor.execute(sql, (arrive, depart, person, roomtype, roomnumber, cellno))
    f = codecs.open("form3.html", 'r')
    print(f.read())


# disconnect from server
db.close()