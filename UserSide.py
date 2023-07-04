from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime as dt
import imageio

import mysql.connector as mc
con=mc.connect(host="localhost",user="root",password="root",database="rcs")
c=con.cursor()

root = Tk()
root.config(bg='navajowhite')
root.geometry("1600x1600")

l = Label(root,bg = "navajowhite").pack()
pic = Image.open("D:\\Data\\OneDrive\\Desktop\\logo.png")
pic = pic.resize((270,270), Image.Resampling.LANCZOS)
pic = ImageTk.PhotoImage(pic)
l = Label(root, image=pic).pack()
l = Label(root,bg = "navajowhite").pack()

l = Label(root, text = "Welcome To Our Retro-Style Coffee Shop!", fg ="brown4",bg="navajowhite", font=("Helvetica","32","bold italic")) 
root.title("JavaJive")
l.config()
l.pack()

global frame
global canvas

def newsignup():
    n=Toplevel(root)
    n.title("SignUp to Join the Brew-Crew")
    n.config(bg='navajowhite')
    n.geometry("1600x1600")

    fname=Label(n, text="Enter firstname:",bg = "navajowhite", font=("times new roman",13,"bold")).pack()
    fname=StringVar() 
    fnameentry = Entry(n, textvariable=fname).pack()

    l = Label(n, text = "",bg = "navajowhite")
    l.pack()

    lname=Label(n, text="Enter lastname:",bg = "navajowhite" ,font=("times new roman",13,"bold")).pack()
    lname=StringVar()
    lnameentry = Entry(n, textvariable=lname).pack()

    l = Label(n, text = "",bg = "navajowhite") 
    l.pack()
    
    username=Label(n, text="Enter username:",bg = "navajowhite",font=("times new roman",13,"bold")).pack()
    username=StringVar()
    usernameentry = Entry(n, textvariable=username).pack()

    l = Label(n, text = "",bg = "navajowhite")
    l.pack()

    phno=Label(n, text="Enter phone number:", bg = "navajowhite",font=("times new roman",13,"bold")).pack()
    phno=StringVar()
    phnoentry = Entry(n, textvariable=phno).pack()

    l = Label(n, text = "",bg = "navajowhite")
    l.pack()

    addr=Label(n, text="Enter address:",bg = "navajowhite", font=("times new roman",13,"bold")).pack()
    addr=StringVar()
    addrentry = Entry(n, textvariable=addr).pack()

    l = Label(n, text = "",bg = "navajowhite")
    l.pack()

    pwd=Label(n, text="Enter password:",bg = "navajowhite", font=("times new roman",13,"bold")).pack()
    pwd=StringVar()
    pwdentry = Entry(n,show=".", textvariable=pwd).pack()

    l = Label(n, text = "",bg = "navajowhite")
    l.pack()

    confpwd=Label(n, text="confirm password",bg = "navajowhite", font=("times new roman",13,"bold")).pack()
    confpwd=StringVar()
    confpwdentry = Entry(n,show=".", textvariable=confpwd).pack()

    l = Label(n, text = "",bg = "navajowhite")
    l.pack()

    n.iconbitmap("D:\\Data\\Downloads\\logo_transparent.ico")
    
    def pcheck():
        p1=pwd.get()
        p2=confpwd.get()

        if p1==p2:
            mes = messagebox.showinfo("","sign up was successful\n login to continue")
            a=("insert into cust values('{}','{}','{}','{}','{}','{}','{}');").format(fname.get(),lname.get(),username.get(),phno.get(),addr.get(),pwd.get(),confpwd.get())
            c.execute(a)
            con.commit()
            
            
        else:
            mes = messagebox.showwarning("warning","passwords don't match")
            bab = Button(n, text = "Try Again!", fg ="white", bg = "black", command = newsignup)
    
    myfont=font.Font(family="helvetica", size=10, weight="bold")
    b = Button(n, text = "submit", fg ="white", bg = "black", command = pcheck)
    b["font"]=myfont
    b.pack()

sel = list()

def newlogin():
    root.destroy()
    n=Tk()
    n.title("Auwana login Page")
    n.config(bg='navajowhite')
    n.geometry("1600x1600")

    username=Label(n, text="username",bg='navajowhite', font=("times new roman",13,"bold")).pack()
    username=StringVar()
    usernameentry = Entry(n, textvariable=username).pack()

    l = Label(n, text = "",bg='navajowhite')
    l.pack()

    pwd=Label(n, text="password",bg='navajowhite', font=("times new roman",13,"bold")).pack()
    pwd=StringVar()
    pwdentry = Entry(n, textvariable=pwd).pack()

    l = Label(n, text = "",bg='navajowhite')
    l.pack()
    n.iconbitmap("D:\\Data\\Downloads\\logo_transparent.ico")

    def lcheck():
        q="select username,pwd from cust;"
        c.execute(q)
        result=c.fetchall()
        con.commit()
        
        u1=username.get()
        p1=pwd.get()
        r="no"
            
        for i in result:
            if i[0]==u1 and i[1]==p1:
                mes = messagebox.showinfo("","login was successful")
                r="yes"
                
                a = Toplevel()
                a.title("Auwana Home Page")
                a.config(bg='navajowhite')
                a.geometry("1600x1600")

                l=Label(a, text = "Auwana", fg ="brown4", bg = "navajowhite", font=("Helvetica","48","bold")).pack()
                im=Image.open("D:\\Data\\Downloads\\search.jpeg")
                im = im.resize((50,50), Image.Resampling.LANCZOS)
                ph=ImageTk.PhotoImage(im)            


                """
                imag=Image.open("D:\\Data\\Downloads\\helpline123.jpeg")#frame
                imag=imag.resize((200,250),Image.Resampling.LANCZOS)
                imag=ImageTk.PhotoImage(imag)
                fr=Frame(a)
                ca=Canvas(fr,width=1250,height=610)
                ca.pack(anchor=S)
                fr.pack(anchor=S)
                ca.create_image(100,250,image=imag)

                pict=Image.open("D:\\Data\\Downloads\\WhatsApp Image 2022-10-22 at 7.37.18 AM.jpeg")#frame2
                pict=pict.resize((150,150),Image.Resampling.LANCZOS)
                pict=ImageTk.PhotoImage(pict)
                ca.create_image(1150,250,image=pict)
                """
                
                video = imageio.get_reader("D:\\Data\\Downloads\\_hitpaw.com (online-video-cutter.com).mp4")#video
                delay = int(1000 / video.get_meta_data()['fps'])
     
                def stream(label):
 
                    try:
                        image = video.get_next_data()
                    except:
                        video.close()
                        return
                    label.after(delay, lambda: stream(label))
                    frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                    label.config(image=frame_image)
                    label.image = frame_image

                if __name__ == '__main__':

                    root=a
                    my_label = Label(root)
                    my_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                    my_label.after(delay, lambda: stream(my_label))
                         
                i=Image.open("D:\\Data\\Downloads\\three-line-menu-icon-11.jpeg")
                i = i.resize((50,50), Image.Resampling.LANCZOS)
                p=ImageTk.PhotoImage(i)

                ima=Image.open("D:\\Data\\Downloads\\cart.jpg")
                ima = ima.resize((50,50), Image.Resampling.LANCZOS)
                pho=ImageTk.PhotoImage(ima)

                image=Image.open("D:\\Data\\Downloads\\helpline123.jpeg")
                image = image.resize((50,50), Image.Resampling.LANCZOS)
                photo=ImageTk.PhotoImage(image)

                a.iconbitmap("D:\\Data\\Downloads\\logo_transparent.ico")

                def helpline():
                    global y
                    n.destroy()
                    y=Tk()
                    y.geometry("1600x1600")
                    y.title("Helpline")
                    y.iconbitmap("D:\\Data\\Downloads\\logo_transparent.ico")
                   
                    f = open("C:\gigi\Python\Python38\MedPharm-Helpline.txt",'r',encoding='UTF8')
                    scroll()
                    global frame
                    f=open("C:\gigi\Python\Python38\MedPharm-Helpline.txt",'r',encoding='UTF8')
                    v=f.read()
                    Label(frame,text=v,fg="black",bg = "navajowhite",font=("calibri",18), justify=LEFT, wraplength=1250).pack()

                def myfunction(event):
                    global canvas
                    canvas.configure(scrollregion=canvas.bbox("all"),width=1250,height=630) 

                def scroll():
                    global y; global frame; global canvas
                    myframe=Frame(y,relief=GROOVE,width=1200,height=630,bd=1)
                    myframe.grid(row=1,column=1)

                    canvas=Canvas(myframe)
                    frame=Frame(canvas)
                    myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
                    canvas.configure(yscrollcommand=myscrollbar.set)
                    myscrollbar.pack(side="right",fill="y")
                    canvas.pack(side="left")
                    canvas.create_window((0,0),window=frame,anchor='nw')
                    frame.bind("<Configure>",myfunction )
                    

                def b1():
                    n.destroy()
                    x=Tk()
                    x.geometry("1600x1600")
                    x.title("Search")
                    x.iconbitmap("D:\\Data\\Downloads\\logo_transparent.ico")

                    
                    class Application(Frame):

                        def __init__(self, master=None):

                            Frame.__init__(self, master)

                            self.pack()
                            self.create_widgets()

                        def CurSelect(self,evt):

                            global sel
                            temp = list()

                            for i in self.lbox.curselection():
                                temp.append(self.lbox.get(i))

                            allitems = list()

                            for i in range(self.lbox.size()):
                                allitems.append(self.lbox.get(i))

                            for i in sel:
                                if i in allitems:
                                    if i not in temp:
                                        sel.remove(i)

                            for x in self.lbox.curselection():
                                if self.lbox.get(x) not in sel:
                                    sel.append(self.lbox.get(x))

                        def select(self):
                            global sel
                            s=', '.join(map(str,sel))
                            self.cursel.set('Current Selection: '+s)
                            
                        def create_widgets(self):
                            self.search_var = StringVar()
                            self.search_var.trace("w", lambda name, index, mode: self.update_list())
                            self.entry =  Entry(self, textvariable=self.search_var, width=300,font=("times new roman",18))

                            self.entry.pack(ipady=10)
                            
                            self.l = Label(self, text = "")
                            self.l.pack()

                            self.lbox = Listbox(self, selectmode=MULTIPLE,width=250, height=18,font=("times new roman",18))
                            self.lbox.bind('<<ListboxSelect>>',self.CurSelect)
                            self.lbox.pack()

                            def cs():
                                sele=self.lbox.curselection()
                                st=[]
                                for i in sele:
                                    e=self.lbox.get(i)
                                    st.append(e)
                                
                                def order():
                                    p=Toplevel(self)
                                    p.geometry("1600x1600")
                                    p.title("Order")
                                    p.iconbitmap("D:\\Data\\Downloads\\logo_transparent.ico")
                                    
                                    z=0
                                    y=1
                                    l=tk.Label(p,text="Order",font=("times new roman",28,"bold")).grid(row=0, column=1)
                                    p.grid_columnconfigure(0, weight=2)
                                    l=tk.Label(p,text="Quantity",font=("times new roman",28,"bold")).grid(row=0, column=4)
                                    p.grid_columnconfigure(3, weight=1)
                                    
                                    for i in sele:
                                        l=tk.Label(p,text=st[z],font=("times new roman",24)).grid(row=y, column=1, ipadx=5, ipady=5, sticky=W)
                                        p.grid_columnconfigure(0, weight=1)
                                        y+=1
                                        z+=1

                                    d={}
                                    x=1
                                    for i in sele:
                                        d["li{0}".format(i)]=IntVar()
                                        la=Label(p,text="\t\t\t")
                                        la.grid(row=x, column=2, ipadx=2, ipady=4)
                                        p.grid_columnconfigure(3, weight=1)
                                        lent=tk.Entry(p, textvariable=d["li{0}".format(i)])
                                        lent.grid(row=x, column=4, ipadx=2, ipady=4)
                                        p.grid_columnconfigure(5, weight=1)
                                        x+=1

                                    def bill():

                                        today=dt.now()
                                        t=today.strftime("%d/%m/%Y")
                                        
                                        for i in sele:
                                            e=self.lbox.get(i)
                                            q=("update menu set qty=qty-{} where bname='{}';").format(d["li{0}".format(i)].get(),e)
                                            c.execute(q)
                                            con.commit()

                                        q=("select fname from cust where username='{}';").format(u1)
                                        c.execute(q)
                                        result=c.fetchall()
                                        con.commit()
                                        for i in result:
                                            x=i[0]

                                        p.destroy()
                                        top=Tk()
                                        top.geometry("1600x1600")
                                        top.title("Bill")
                                        top.iconbitmap("D:\\Data\\Downloads\\logo_transparent.ico")

                                        def myfunction(event):
                                            canvas.configure(scrollregion=canvas.bbox("all"),width=1250,height=630)


                                        def scroll():
                                            global frame
                                            global canvas
                                            myframe=Frame(top,relief=GROOVE,width=500,height=100,bd=1)
                                            myframe.grid(row=1,column=1)

                                            canvas=Canvas(myframe)
                                            frame=Frame(canvas)
                                            myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
                                            canvas.configure(yscrollcommand=myscrollbar.set)
                                            myscrollbar.pack(side="right",fill="y")
                                            canvas.pack(side="left")
                                            canvas.create_window((0,0),window=frame,anchor='nw')
                                            frame.bind("<Configure>",myfunction)
                                        scroll()
                                        global frame
                                        global canvas

                                        l=tk.Label(frame,text="JavaJive",font=("times new roman",28,"bold")).grid(row=0, column=4)
                                        frame.grid_columnconfigure(0, weight=1)
                                        frame.grid_columnconfigure(10, weight=1)
                                        l=tk.Label(frame,text="phone:044-12345678",font=("times new roman",22)).grid(row=1, column=0, sticky=W)
                                        l=tk.Label(frame,text="date:"+t,font=("times new roman",22)).grid(row=2, column=0, sticky=W)
                                        l=tk.Label(frame,text="customer name:"+ str(x),font=("times new roman",22)).grid(row=1, column=10)
                                        l=tk.Label(frame,text="bill no:"+ '10146',font=("times new roman",22)).grid(row=2, column=10)
                                        
                                        l=Label(frame, text=" ", padx=10, pady=3).grid(row=3, column=0)
                                        
                                        frame.grid_columnconfigure(0, weight=0)
                                        frame.grid_columnconfigure(1, weight=1)
                                        frame.grid_columnconfigure(3, weight=1)
                                        frame.grid_columnconfigure(5, weight=1)
                                        frame.grid_columnconfigure(7, weight=1)
                                        frame.grid_columnconfigure(9, weight=1)
                                        frame.grid_columnconfigure(11, weight=1)
                                        
                                        l=tk.Label(frame,text="Order",font=("times new roman",24,"bold")).grid(row=4, column=0)
                                        
                                        l=tk.Label(frame,text="Cost",font=("times new roman",24,"bold")).grid(row=4, column=2)

                                        z=0
                                        y=5
                                        for i in sele:
                                            l=tk.Label(frame,text=st[z],font=("times new roman",24))
                                            l.grid(row=y, column=0, ipadx=5, ipady=5)
                                            frame.grid_columnconfigure(1, weight=1)
                                            y+=1
                                            z+=1

                                        y=5
                                        for i in d:
                                            l=tk.Label(frame, text=d[i].get(),font=("times new roman",24)).grid(row=y, column=2, ipadx=5, ipady=5)
                                            y+=1

                                        z=0
                                        x=5
                                        for i in sele:
                                            q=("select bcat from menu where bname='{}';").format(st[z])
                                            c.execute(q)
                                            result=c.fetchall()
                                            con.commit()
                                            l=tk.Label(frame,text=result,font=("times new roman",24)).grid(row=x, column=4)
                                            z+=1
                                            x+=1

                                        z=0
                                        x=5
                                        for i in sele:
                                            #q=("select Members from stock where Destination='{}';").format(st[z])
                                            #c.execute(q)
                                            result="Skimmed Milk"
                                            con.commit()
                                            l=tk.Label(frame,text=result,font=("times new roman",24)).grid(row=x, column=6)
                                            z+=1
                                            x+=1

                                        z=0
                                        x=5
                                        for i in sele:
                                            q=("select bcost from menu where bname='{}';").format(st[z])
                                            c.execute(q)
                                            result=c.fetchone()
                                            con.commit()
                                            for j in result:
                                                res=j
                                            l=tk.Label(frame,text=result,font=("times new roman",24)).grid(row=x, column=8)
                                            z+=1
                                            x+=1


                                        fdf=0
                                        z=0
                                        x=5
                                        for i in sele:
                                            q=("select bcost from menu where bname='{}';").format(st[z])
                                            c.execute(q)
                                            result=c.fetchone()
                                            con.commit()
                                            for j in result:
                                                res=j
                                                price=d["li{0}".format(i)].get()*res
                                                fdf+=int(price)
                                                fdf=(fdf*12/100)+(fdf*12/100)+fdf#sgst+cgst+invoicetotal
                                                global customerprice
                                                customerprice=fdf
                                            z+=1
                                            x+=1
                                        l=tk.Label(frame,text=str(fdf)+'.00',font=("times new roman",24,'bold')).grid(row=x, column=10)

                                        frame.grid_rowconfigure(3, weight=1)

                                        l=tk.Label(frame,text="Bcat",font=("times new roman",24,"bold")).grid(row=4, column=4)
                                        l=tk.Label(frame,text=" Type of Milk ",font=("times new roman",24,"bold")).grid(row=4, column=6)
                                        l=tk.Label(frame,text="Bcost",font=("times new roman",24,"bold")).grid(row=4, column=8)
                                        l=tk.Label(frame,text="Tot.Cost",font=("times new roman",24,"bold")).grid(row=4, column=10)

                                        frame.grid_rowconfigure(y, weight=4)

                                        def info():
                                        
                                             mes= messagebox.showinfo('','Check customer points credited to your account(;\nyour order will be arriving soon!')

                                        but=tk.Button(frame,text="Confirm Purchase",font=("times new roman",18), command=info).grid(row=x+1,column=10)
                                        
                                    b=tk.Button(p, text="proceed", command=bill)
                                    b.grid(row=x, column=2)
                                    p.grid_columnconfigure(0, weight=2)
                                    p.grid_columnconfigure(3, weight=1)
                                    p.grid_columnconfigure(5, weight=2)

                                order()

                            self.btn=Button(self,text='Place Order', command=cs, width=20)
                            self.btn.pack(anchor=CENTER, side=RIGHT)

                            self.la=Label(self,text="\t")
                            self.la.pack(side=RIGHT)

                            #self.btn=Button(self,text='Add to cart', width=20)
                            #self.btn.pack(side=RIGHT)

                            self.cursel=StringVar()
                            self.lb1=Label(self,textvariable=self.cursel)
                            self.lb1.pack()

                            self.update_list()

                        def update_list(self):
                            global sel
                            global l
                            search_term = self.search_var.get()

                            q="select bname from menu;"
                            c.execute(q)
                            result = c.fetchall()
                            res = [''.join(i) for i in result]
                            con.commit()
                            
                            lbox_list = res

                            self.lbox.delete(0, END)

                            for item in lbox_list:
                                    if search_term.lower() in item.lower():
                                        self.lbox.insert(END, item)

                            allitems=list()
                            for i in range(self.lbox.size()):
                                allitems.append(self.lbox.get(i))

                            for i in sel:
                                if i in allitems:
                                    self.lbox.select_set(self.lbox.get(0, "end").index(i))
                                          
                    app = Application(master=x)
                    app.mainloop()

                b1=tk.Button(a, image=ph, command=b1).place(relx=1.0, x=0,y=-1, anchor=NE)
                #b2=tk.Button(a,image=p).place(x=0,y=0)
                #b3=tk.Button(a, image=pho).place(relx=0.91, x=0, y=-1)
                #b4=tk.Button(a, image=photo, command= helpline).place(relx=0.86, x=0, y=-3)
                b4=tk.Button(a, image=photo, command= helpline).place(x=0, y=0)
                                
                a.mainloop()

        if r=="no":
            mes = messagebox.showerror("error","login was unsuccessful")
            
    b = Button(n, text = "submit", fg ="white", bg = "black", command = lcheck)
    b["font"]=myfont
    b.pack()

l = Label(root, text = "",bg = "navajowhite")
l.pack()
l = Label(root, text = "",bg = "navajowhite")
l.pack()
l = Label(root, text = "",bg = "navajowhite")
l.pack()
l = Label(root, text = "",bg = "navajowhite")
l.pack()

myfont=font.Font(family="helvetica", size=10, weight="bold")
b = Button(root, text = "sign up", fg ="white", bg = "Black", command = newsignup, height = 2)
b["font"]=myfont
b.pack()

l = Label(root, text = "or",fg ="brown4", bg = "navajowhite", font=("times new roman",14,"bold"))
l.pack()

myfont=font.Font(family="helvetica", size=10, weight="bold")
b = Button(root, text = "login", fg ="white", bg = "Black", height=2, command = newlogin)
b["font"]=myfont
b.pack()

"""
imag=Image.open("D:\\Data\\Downloads\\Clinique logo.jpeg")
imag=imag.resize((1000,200),Image.Resampling.LANCZOS)
imag=ImageTk.PhotoImage(imag)
fr=Frame(root)
ca=Canvas(fr,width=1250,height=650)
ca.pack(anchor=SW)
fr.pack(anchor=SW)
ca.create_image(620,200,image=imag)

"""


root.iconbitmap("D:\\Data\\Downloads\\logo_transparent.ico")
root.mainloop()

print("Customer Points Credited to your Account:",int(customerprice//100*10),"!")
