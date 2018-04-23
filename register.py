from Tkinter import *
import time;
import sqlite3
import tkMessageBox

def newuser():

        root=Tk()
        root.geometry("1600x800+0+0")
        root.title("Book Management System")
        root.configure(bg='white')

        Tops=Frame(root, width=1600, height=50, bg="white")
        Tops.pack(side=TOP)

        f1=Frame(root, width=800, height=700, bg="white")
        f1.pack(side=TOP)



        localtime=time.asctime(time.localtime(time.time()))

        lblinfo = Label(Tops, font=('arial', 50 , 'bold' ), text="Book Management System" , fg="midnight blue",bg="white", bd=10,anchor='w')
        lblinfo.grid(row=0,column=0)
        lblinfo = Label(Tops, font=('arial', 20 , 'bold' ), text=localtime , fg="midnight blue",bg="white", bd=10,anchor='w')
        lblinfo.grid(row=1,column=0)


        l2=Label(f1,text="\n\n\n\n",bg="white")
        l2.grid(row=0,column=0)
        L1 = Label(f1, text="Name : ",font=('arial',15,'bold'),fg="midnight blue",bg="white")
        L1.grid(row=1,column=0)
        l3=Label(f1,text="\t\t\t",bg="white")
        l3.grid(row=1,column=1)
        E1 = Entry(f1, bd =5,width=50,font=('arial',10,'bold'),relief="groove")
        E1.grid(row=1,column=2)


        var = IntVar()
        lab = Label(f1, text="\nGender : ",font=('arial',15,'bold'),fg="midnight blue",bg="white")
        lab.grid(row=2,column=0)
        R1 = Radiobutton(f1, text="Male", variable=var, value=1,bg="white",fg="midnight blue",font=('arial',12,'bold'))
        R1.grid(row=2,column=2 )
        R2 = Radiobutton(f1, text="Female", value=2,variable=var,bg="white",fg="midnight blue",font=('arial',12,'bold'))
        R2.grid( row=2,column=3)


        l4=Label(f1,text="\n",bg="white")
        l4.grid(row=3,column=0)
        L2 = Label(f1, text="Address : ",font=('arial',15,'bold'),fg="midnight blue",bg="white")
        L2.grid(row=4,column=0)
        l5=Label(f1,text="\t\t\t",bg="white")
        l5.grid(row=4,column=1)
        E2 = Entry(f1, bd =5,width=50,font=('arial',10,'bold'),relief="groove")
        E2.grid(row=4,column=2)


        l5=Label(f1,text="\n",bg="white")
        l5.grid(row=5,column=0)
        L3 = Label(f1, text="Phone No : ",font=('arial',15,'bold'),fg="midnight blue",bg="white")
        L3.grid(row=6,column=0)
        l6=Label(f1,text="\t\t\t",bg="white")
        l6.grid(row=6,column=1)
        E3 = Entry(f1, bd =5,width=50,font=('arial',10,'bold'),relief="groove")
        E3.grid(row=6,column=2)

        l6=Label(f1,text="\n",bg="white")
        l6.grid(row=7,column=0)
        L4 = Label(f1, text="E-Mail : ",font=('arial',15,'bold'),fg="midnight blue",bg="white")
        L4.grid(row=8,column=0)
        l7=Label(f1,text="\t\t\t",bg="white")
        l7.grid(row=8,column=1)
        E4 = Entry(f1, bd =5,width=50,font=('arial',10,'bold'),relief="groove")
        E4.grid(row=8,column=2)


        l7=Label(f1,text="\n",bg="white")
        l7.grid(row=9,column=0)
        L5 = Label(f1, text="Password : ",font=('arial',15,'bold'),fg="midnight blue",bg="white")
        L5.grid(row=10,column=0)
        l8=Label(f1,text="\t\t\t",bg="white")
        l8.grid(row=10,column=1)
        E5 = Entry(f1, bd =5,width=50,font=('arial',10,'bold'),relief="groove",show="*")
        E5.grid(row=10,column=2)

        
        lab3=Label(f1,text="\n",bg="white")
        lab3.grid(row=9,column=0)
        def takeval():
                        name=E1.get()
                        address=E2.get()
                        phone=E3.get()
                        email=E4.get()
                        passw=E5.get()
                        conn = sqlite3.connect('bms.db')
                        c=conn.cursor()
                        c.execute("insert into user_detail(name,gender,address,phone,email,password) values('"+name+"',"+str(var.get())+",'"+address+"',"+phone+",'"+email+"','"+passw+"');")
                        conn.commit()
                        conn.close()
                        tkMessageBox.showinfo("Registered","Registration Successful")
        B=Button(f1,text="Submit",width=20,font=('arial',10,'bold'),fg="white",bg="midnight blue",command=takeval)
        B.grid(row=14,column=2)

        root.mainloop()
if __name__=="__main__":
        newuser()

