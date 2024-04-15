import psycopg2

def create():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="2756", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE student(ID serial,Name text,Age text,Address text);''')
    print("Table created successfully")
    conn.commit()
    conn.close()

def insert_data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="2756", host="localhost", port="5432")
    cur = conn.cursor()
    name=input("Enter name: ")
    age=input("Enter age: ")
    address=input("Enter address: ")

    querry='''INSERT INTO student (Name,Age,Address) VALUES(%s,%s,%s);'''
    cur.execute(querry,(name,age,address))
    print("Data inserted successfully")
    conn.commit()
    conn.close()

insert_data()
