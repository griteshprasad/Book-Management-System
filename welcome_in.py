from register import *
import tkMessageBox
import sqlite3
from login_page import *
from request_book import *
from books import *

def welcome():

        root=Tk()
        root.geometry("1600x800+0+0")
        root.title("Book Management System")
        root.configure(bg="white")


        Top1=Frame(root, width=1600, height=50, bg="white")
        Top1.pack(side=TOP)

        f1=Frame(root, width=800, height=700, bg="white")
        f1.pack(side=TOP)

        localtime=time.asctime(time.localtime(time.time()))

        conn =sqlite3.connect('bms.db')
        c=conn.cursor()


        lblinfo = Label(Top1, font=('arial', 50 , 'bold' ), text="Book Management System" , fg="midnight blue",bg="white", bd=10,anchor='w')
        lblinfo.grid(row=0,column=0)
        lblinfo = Label(Top1, font=('arial', 20 , 'bold' ), text=localtime , fg="midnight blue",bg="white", bd=10,anchor='w')
        lblinfo.grid(row=1,column=0)

        lab=Label(f1,text="\n\n\n\n\n\n\n\n",bg="white")
        lab.grid(row=0,column=0)
        L1 = Label(f1, text="WELCOME USER!!!",font=('arial',15,'bold'),fg="midnight blue",bg="white")
        L1.grid(row=1,column=1)

        lab=Label(f1,text="\t\t\t",bg="white")
        lab.grid(row=2,column=1)
 
        B4=Button(f1,text="Order",width=20,height=4,bd=5,font=('arial',10,'bold'),fg="white",bg="midnight blue",relief="raised",command=order)
        B4.grid(row=3,column=1)

        lab=Label(f1,text="\t\t\t",bg="white")
        lab.grid(row=3,column=2)

        B5=Button(f1,text="Books Available",width=20,height=4,bd=5,font=('arial',10,'bold'),fg="white",bg="midnight blue",relief="raised",command=book_list)
        B5.grid(row=5,column=1)

        lab=Label(f1,text="\t\t\t",bg="white")
        lab.grid(row=4,column=2)

        root.mainloop()

if __name__=="__main__":
        login()
