import sqlite3
from sqlite3 import Error
def create_cannektion(db_file):
    conn= False
    try:
        conn=sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn



def update_students_mark_is_married(conn,id,mark,married_status):
    sql=''' UPDATE student SET mark =?,is_married=? WHERE id =?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,(mark,married_status,id))
        conn.commit()
    except Error as e:
        print(e)

def create_table(conn,sql):
    try:
        cursor=conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def rekud_students(conn):
    try:
        sql='''SELECT * FROM student'''
        cursor= conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)

def create_student(conn,student):
    sql='''INSERT INTO student(full_name,mark,hobby,birth_date,is_married)
    VALUES (?,?,?,?,?)
    '''
    try:
        cursor=conn.cursor()
        cursor.execute(sql,student)
        conn.commit()
    except Error as e:
        print(e)


database= r'group_24.db'


sql_create_student_table='''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR (50) NOT NULL ,
mark DOUBLE (5,2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
);
'''
connektion= create_cannektion(database)

if connektion is not None:
    print("Все работает")
    # create_table(connektion,sql_create_student_table)
    # create_student(connektion,('Sultan',10,'ПЛАВАНИЕ' ,'20.08.2006',True))
    rekud_students(connektion)
    update_students_mark_is_married(connektion,1,5,False)
    rekud_students(connektion)