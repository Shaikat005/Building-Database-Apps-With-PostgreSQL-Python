from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()

def get_data(name,age,address):
     conn = psycopg2.connect(dbname="postgres", user="postgres", password="2756", host="localhost", port="5432")
     cur = conn.cursor()
     querry='''INSERT INTO student (Name,Age,Address) VALUES(%s,%s,%s);'''
     cur.execute(querry,(name,age,address))
     conn.commit()
     conn.close()
     display_all()
     print("Data entered successfully")

def search(id):
     conn = psycopg2.connect(dbname="postgres", user="postgres", password="2756", host="localhost", port="5432")
     cur = conn.cursor()
     query = '''SELECT * FROM student WHERE id =%s;'''
     cur.execute(query,(id))
     row = cur.fetchone()
     display_search(row)
     conn.commit()
     conn.close()

def display_search(row):
     listbox = Listbox(frame,width=20,height=1,font=("",14))
     listbox.grid(row=9,column=1)
     listbox.insert(END,row)

def display_all():
     conn = psycopg2.connect(dbname="postgres", user="postgres", password="2756", host="localhost", port="5432")
     cur = conn.cursor()  
     query = '''SELECT * from student''' 
     cur.execute(query)
     row = cur.fetchall()

     listbox = Listbox(frame,width=20,height=5,font=("",14))
     listbox.grid(row=10,column=1)
     for x in row:
        listbox.insert(END,x)





canvas = Canvas(root,width=900,height=480)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

label = Label(frame,text="Add data",font=("",14))
label.grid(row=0,column=1)

label = Label(frame,text="Name",font=("",14))
label.grid(row=1,column=0)
entry_name = Entry(frame,font=("",14))
entry_name.grid(row=1,column=1)

label = Label(frame,text="Age",font=("",14))
label.grid(row=2,column=0)
entry_age = Entry(frame,font=("",14))
entry_age.grid(row=2,column=1)

label = Label(frame,text="Address",font=("",14))
label.grid(row=3,column=0)
entry_address = Entry(frame,font=("",14))
entry_address.grid(row=3,column=1)

button = Button(frame,text="Add",font=("",14),command=lambda :get_data(entry_name.get(),entry_age.get(),entry_address.get()))
button.grid(row=4,column=1)

label = Label(frame,text="Search Data",font=("",14))
label.grid(row=5,column=1)

label = Label(frame,text="Search by ID",font=("",14))
label.grid(row=6,column=0)
id_search = Entry(frame,font=("",14))
id_search.grid(row=6,column=1)

button = Button(frame,text="Search",font=("",14),command=lambda:search(id_search.get()))
button.grid(row=6,column=2)


root.mainloop()