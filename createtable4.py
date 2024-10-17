import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sandra23',
    database='kerala45'
)
mycursor=mydb.cursor()
sql='''CREATE TABLE courses(
    id int AUTO_INCREMENT primary key,
    course_name varchar(255) not null,
    course_code varchar(10) not null unique
    )'''    
mycursor.execute(sql)

sql = "INSERT INTO courses (course_name, course_code) VALUES (%s, %s)"
val = [
    ('Computer Science', 'CS101'),
    ('Mathematics', 'MATH102'),
    ('Physics', 'PHYS103'),
    ('Chemistry', 'CHEM104'),
    ('Physics', 'PHYS103'),
    ('Chemistry', 'CHEM104'),
    ('Biology', 'BIO105')
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,'record inserted.')
