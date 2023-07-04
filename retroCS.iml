#ADMIN SIDE:

import mysql.connector as mc
from mysql.connector import MySQLConnection as msc
from tabulate import tabulate as tb
con=mc.connect(host="localhost",user="root",password="root",database="rcs")
c=con.cursor(buffered=True)

adminpwd="admin"
p=input("enter key")

while p=="admin":
    print("welcome! what do you wanna view")
    print("1.order details\n2.sales details\n3.customer details\n4.menu\n5.exit")
    ch=int(input("enter your choice"))
    if ch==1:
        q=("select * from ord order by oid;")
        c.execute(q)
        a=c.fetchall()
        print(tb(a, headers = ["oid","bname","bcost","qty","tcost","fcag"], tablefmt='psql'))
        con.commit()
        print("do you wanna update, delete, search or insert a row")
        b=input("enter your choice")
        
        if b=="update":
            print("what col do u wanna update")
            ch=input("enter col name")
            
            if ch=="bname":
        
                def update(n,r): 
                    dat=(n,r)
                    q="update ord set bname = %s where oid = %s;"   
                    c.execute(q,dat)
                    con.commit()
                r=int(input("enter oid"))
                n=int(input("enter new data"))
                update(n,r)
        
            elif ch=="qty":
        
                def update(n,r): 
                    dat=(n,r)
                    q="update ord set quantity = %s where oid = %s;"   
                    c.execute(q,dat)
                    con.commit()
                r=int(input("enter oid"))
                n=int(input("enter new data"))
                update(n,r)    

            elif ch=="bcost":
        
                def update(n,r):
                    q="update ord set bcost = %s where oid = %s;"
                    dat=(n,r)
               
                    c.execute(q,dat)
                    con.commit()
                r=int(input("enter oid"))
                n=int(input("enter new data"))
                update(n,r)

            elif ch=="tcost":
        
                def update(n,r): 
                    dat=(n,r)
                    q="update ord set tcost = %s where oid = %s;"  
                    c.execute(q,dat)
                    con.commit()
                r=input("enter oid")
                n=input("enter new data")
                update(n,r)

            elif ch=="fcag":
        
                def update(n,r): 
                    dat=(n,r)
                    q="update ord set fcag = %s where oid = %s;"  
                    c.execute(q,dat)
                    con.commit()
                r=input("enter oid")
                n=input("enter new data")
                update(n,r)    

        elif b=="delete":
            print("which row do you wanna delete")
            o=input("enter oid")
            q=("delete from ord where oid='{}';").format(o)
            c.execute(q)
            con.commit()

        elif b=="search":
            print("what do you wanna search for")
            o=input("enter order id")
            q=("select * from ord where oid='{}';").format(o)
            c.execute(q)
            a=c.fetchone()
            print(*a)
            con.commit()

        elif b=="insert a row":
            a=input("enter oid")
            b=input("enter bname")
            f=input("enter bcost")
            d=input("enter qty")
            e=input("enter tcost")
            g=input("enter fcag")
            q=("insert into ord values('{}','{}','{}','{}','{}','{}');").format(a,b,f,d,e,g)
            c.execute(q)
            con.commit()
                
    elif(ch==2):
        q=("select * from sales")
        c.execute(q)
        a=c.fetchall()
        print(tb(a, headers = ["sid","tdate","bname","custc"], tablefmt='psql'))
        con.commit()

        print("do you wanna update, delete, search or insert a row")
        b=input("enter your choice")
        
        if b=="update":
            print("what col do u wanna update")
            ch=input("enter col name")
        
            if ch=="bname":
        
                def update(n,r): 
                    dat=(n,r)
                    q="update sales set bname = %s where sid = %s;"  
                    c.execute(q,dat)
                    con.commit()

                r=int(input("enter  sid"))
                n=int(input("enter new data"))
                update(n,r)    

            elif ch=="tdate":
        
                def update(n,r):
                    q="update sales set tdate = %s where sid = %s;"
                    dat=(n,r)
               
                    c.execute(q,dat)
                    con.commit()

                r=int(input("enter sid"))
                n=int(input("enter new data"))
                update(n,r)

            elif ch=="custc":
        
                def update(n,r):
                    q="update sales set custc = %s where sid = %s;"
                    dat=(n,r)
               
                    c.execute(q,dat)
                    con.commit()

                r=int(input("enter sid"))
                n=int(input("enter new data"))
                update(n,r)

        elif b=="delete":
            print("which row do you wanna delete")
            o=input("enter sid")
            q=("delete from sales where sid='{}';").format(o)
            c.execute(q)
            con.commit()

        elif b=="search":
            print("who do you wanna search for")
            o=input("enter sid")
            q=("select * from sales where sid='{}';").format(o)
            c.execute(q)
            a=c.fetchone()
            print(*a)
            con.commit()

        elif b=="insert a row":
            a=input("enter tdate")
            b=input("enter bname")
            f=input("enter custc")
            d=input("enter sid")
            q=("insert into sales values('{}','{}','{}','{}');").format(a,b,f,d)
            c.execute(q)
            con.commit()
            
    elif ch==3:
        q=("select * from cust")
        c.execute(q)
        a=c.fetchall()
        print(tb(a, headers = [ "cid","lname","fname","address","Cpoints","username","password","confpwd"], tablefmt='psql'))
        con.commit()
        
    elif ch==4:
        q=("select * from menu")
        c.execute(q)
        a=c.fetchall()
        print(tb(a, headers = [ "bname","bcat","bcost","qty"], tablefmt='psql'))
        print("do you wanna add or delete an order")
        ch=input("enter your choice")

        if ch=="add":
            a=input("enter bname")
            f=input("enter bcat")
            d=input("enter bcost")
            e=input("enter qty/day")

            q=("insert into menu(bname,bcat,bcost,qty) values('{}','{}','{}','{}');").format(a,f,d,e)
            c.execute(q)
            con.commit()

        elif ch=='delete':
            print("what record do you wanna delete")
            a=input("enter bname")

            q=("delete from menu where bname='{}';").format(a)
            c.execute(q)
            con.commit()

    elif ch==5:
         break

con.close()
c.close()


