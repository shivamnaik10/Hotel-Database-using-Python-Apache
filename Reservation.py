#!C:/Rutgers/Sem 1/BDM/Project/BDM project/venv/Scripts/python.exe
print("Content-Type: text/html")
print()
import cgi,cgitb
import codecs
cgitb.enable() #for debugging
form1 = cgi.FieldStorage()
email = form1.getvalue('email')
name = form1.getvalue('psw')
Phone = form1.getvalue('phone')


f=codecs.open("form1.html", 'r')
print(f.read())