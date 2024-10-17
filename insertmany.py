import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="sandra23",
                             database="kerala45")
mycursor=mydb.cursor()

sql="INSERT INTO student(name,address) VALUES (%s ,%s)"
val=[("sandra","ddd,ktm"),("amna","rrr,ekm"),("Aishwarya","bbb,khf"),("adithya","fgd,khg")]

mycursor.executemany(sql,val)
mydb.commit()

print(mycursor.rowcount,"was inserted.")
