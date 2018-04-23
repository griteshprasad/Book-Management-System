import time;
from Tkinter import *
from tkMessageBox import *
import sqlite3

def order():

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


        lab=Label(f1,text="\n\n\n\n\n\n\n\n",bg="white")
        lab.grid(row=0,column=0)
        L1 = Label(f1, text="Book Name : ",font=('arial',15,'bold'),fg="midnight blue",bg="white")
        L1.grid(row=1,column=0)
        lab=Label(f1,text="\t",bg="white")
        lab.grid(row=1,column=1)
        E1 = Entry(f1, bd =5,width=40,font=('arial',10,'bold'),relief="groove")
        E1.grid(row=1,column=2)


        

        def ordered():
                conn =sqlite3.connect('bms.db')
                c=conn.cursor()
                deta =c.execute("SELECT * from booklist")
                flag=0
                for row in deta:
                        for i in range(0,11):
                                if (row[i] ==E1.get()):
                                        flag =1
                                        break
                if(flag ==1):
                        showinfo('Ordered','Book ordered Successfully')
                else:
                        showinfo('Unavailable','Book Not Available')

        lab=Label(f1,text="\n\n\n\n",bg="white")
        lab.grid(row=3,column=0)
        B=Button(f1,text=" Order ",width=20,bd=5,font=('arial',10,'bold'),fg="white",bg="midnight blue",relief="raised",command=ordered)
        B.grid(row=3,column=2)

        root.mainloop()
