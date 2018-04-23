from Tkinter import *
from login_page import *
from register import *
from request_book import *
import time;



def ask_quit():
    if tkMessageBox.askokcancel("Quit", "You want to quit now?"):
        root.destroy()


import sqlite3
conn = sqlite3.connect('bms.db')
c=conn.cursor()
##c.execute("CREATE TABLE USER_DETAIL (NAME text,GENDER real ,ADDRESS text,PHONE real,EMAIL text,PASSWORD text)")
conn.commit()
conn.close()

root=Tk()
root.geometry("1600x800+0+0")
root.title("Book Management System")
root.configure(bg="white")


Tops=Frame(root, width=1600, height=50, bg="white")
Tops.pack(side=TOP)

f1=Frame(root, width=800, height=700, bg="white")
f1.pack(side=TOP)

localtime=time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font=('arial', 50 , 'bold' ), text="Book Management System" , fg="midnight blue",bg="white", bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=('arial', 20 , 'bold' ), text=localtime , fg="midnight blue",bg="white", bd=10,anchor='w')
lblinfo.grid(row=1,column=0)


lab=Label(f1,text="\n\n\n\n\n\n\n\n\n\n",bg="white")
lab.grid(row=0,column=0)

B1=Button(f1,text="Login",width=20,height=4,bd=5,font=('arial',10,'bold'),fg="white",bg="midnight blue",relief="raised",command=login)
B1.grid(row=1,column=0)

lab=Label(f1,text="\t\t\t",bg="white")
lab.grid(row=1,column=1)


B2=Button(f1,text="New User",width=20,height=4,bd=5,font=('arial',10,'bold'),fg="white",bg="midnight blue",relief="raised",command=newuser)
B2.grid(row=1,column=2)

lab=Label(f1,text="\t\t\t",bg="white")
lab.grid(row=1,column=3)


B4=Button(f1,text="Order",width=20,height=4,bd=5,font=('arial',10,'bold'),fg="white",bg="midnight blue",relief="raised",command=order)
B4.grid(row=1,column=6)

lab=Label(f1,text="\t\t\t",bg="white")
lab.grid(row=1,column=7)

B4=Button(f1,text="Quit",width=20,height=4,bd=5,font=('arial',10,'bold'),fg="white",bg="midnight blue",relief="raised",command=ask_quit)
B4.grid(row=1,column=8)

lab=Label(f1,text="\t",bg="white")
lab.grid(row=1,column=9)


root.mainloop()
