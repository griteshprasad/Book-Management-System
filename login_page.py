from register import *
import tkMessageBox
import sqlite3
from welcome_in import *


def login():

        root=Tk()
        root.geometry("1600x800+0+0")
        root.title("Book Management System")
        root.configure(bg="white")


        Top1=Frame(root, width=1600, height=50, bg="white")
        Top1.pack(side=TOP)

        f1=Frame(root, width=800, height=700, bg="white")
        f1.pack(side=TOP)

        localtime=time.asctime(time.localtime(time.time()))

        lblinfo = Label(Top1, font=('arial', 50 , 'bold' ), text="Book Management System" , fg="midnight blue",bg="white", bd=10,anchor='w')
        lblinfo.grid(row=0,column=0)
        lblinfo = Label(Top1, font=('arial', 20 , 'bold' ), text=localtime , fg="midnight blue",bg="white", bd=10,anchor='w')
        lblinfo.grid(row=1,column=0)

        lab=Label(f1,text="\n\n\n\n\n\n\n\n",bg="white")
        lab.grid(row=0,column=0)
        L1 = Label(f1, text="User Name : ",font=('arial',15,'bold'),fg="midnight blue",bg="white")
        L1.grid(row=1,column=0)
        lab=Label(f1,text="\t",bg="white")
        lab.grid(row=1,column=1)
        E1 = Entry(f1, bd =5,width=40,font=('arial',10,'bold'),relief="groove")
        E1.grid(row=1,column=2)


        lab=Label(f1,text="\n\n\n\n\n\n",bg="white")
        lab.grid(row=2,column=0)
        L2 = Label(f1, text="Password : ",font=('arial',15,'bold'),fg="midnight blue",bg="white")
        L2.grid(row=2,column=0)
        lab=Label(f1,text="\t",bg="white")
        lab.grid(row=2,column=1)
        E2 = Entry(f1, bd =5,width=40,font=('arial',10,'bold'),relief="groove",show="*")
        E2.grid(row=2,column=2)

        def submit():
                conn =sqlite3.connect('bms.db')
                c=conn.cursor()
                deta =c.execute("SELECT NAME , PASSWORD FROM USER_DETAIL")
                flag=0
                for row in deta:
                        if (row[0] ==E1.get() and row[1] ==E2.get()):
                                flag =1
                                break
                if(flag ==1):
                        tkMessageBox.showinfo('SUCCESS','LOGIN SUCCESSFUL')
                        welcome();
                else:
                        tkMessageBox.showinfo('LOGIN DENIED','INCORRECT DETAILS')
        B1=Button(f1,text="Login",width=20,bd=5,font=('arial',10,'bold'),fg="white",bg="midnight blue",relief="raised",command=submit)
        B1.grid(row=3,column=2)

        lab=Label(f1,text="\n\n\n\n\n",bg="white")
        lab.grid(row=4,column=4)

        B2=Button(f1,text="New User",width=20,bd=5,font=('arial',10,'bold'),fg="white",bg="midnight blue",relief="raised",command=newuser)
        B2.grid(row=4,column=2)

        root.mainloop()

if __name__=="__main__":
        login()
