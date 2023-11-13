import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root", passwd="admin",database="abhijith" )
mycusor = mydb.cursor()
mycusor.execute("select * from abhi")
result = mycusor.fetchall()
for i in result:
    print(i)  