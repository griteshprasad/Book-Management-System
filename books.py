from register import *
import tkMessageBox
import sqlite3
from login_page import *
from request_book import *
from welcome_in import *

def book_list():

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

        listbook=['The Girl on The Train','Believe in Yourself','If Its Not Forever','One Indian Girl','It Happens For A Reason','The Secret','The Great Indian Diet','Our Impossible Love','When Only Love Remains','The White Tiger','Sea Of Poppies']

        conn = sqlite3.connect('bms.db')
        c=conn.cursor()
        #c.execute('create table booklist(book1 text,book2 text,book3 text,book4 text,book5 text,book6 text,book7 text,book8 text,book9 text,book10 text,book11 text)')
        c.execute("insert into booklist values (?,?,?,?,?,?,?,?,?,?,?)",listbook)
        conn.commit()
        conn.close()
    

        lblinfo = Label(Top1, font=('arial', 50 , 'bold' ), text="Book Management System" , fg="midnight blue",bg="white", bd=10,anchor='w')
        lblinfo.grid(row=0,column=0)
        lblinfo = Label(Top1, font=('arial', 20 , 'bold' ), text=localtime , fg="midnight blue",bg="white", bd=10,anchor='w')
        lblinfo.grid(row=1,column=0)

        lab=Label(f1,text="\n\n\n\n\n\n\n\n",bg="white")
        lab.grid(row=0,column=0)

        L1 = Label(f1, text="BOOKS",font=('arial',12,'bold'),fg="midnight blue",bg="white")
        L1.grid(row=0,column=1)
        L4 = Label(f1, text="PRICE(in Rs)",font=('arial',12,'bold'),fg="midnight blue",bg="white")
        L4.grid(row=0,column=2)

        L3 = Label(f1, text="The Girl on The Train\nBelieve in Yourself\nIf Its Not Forever\nOne Indian Girl\nIt Happens For A Reason\nThe Secret\nThe Great Indian Diet\nOur Impossible Love\nWhen Only Love Remains\nThe White Tiger\nSea Of Poppies",font=('arial',12),fg="midnight blue",bg="white")
        L3.grid(row=2,column=1)
        L5 = Label(f1, text="437\n69\n88\n95\n100\n369\n149\n89\n108\n395\n599",font=('arial',12),fg="midnight blue",bg="white")
        L5.grid(row=2,column=2)


        lab=Label(f1,text="\t\t\t",bg="white")
        lab.grid(row=4,column=3)


        root.mainloop()

if __name__=="__main__":
        login()
