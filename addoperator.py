import mysql.connector
from tkinter import *
from tkinter.messagebox import *
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd="Danger@66",\
                             database="bus_booking")
mycursor=mydb.cursor()
def operatoradd():
    L=[]
    op_id=o_id.get()
    L.append(op_id)
    name=op_name.get()
    L.append(name)
    address=op_address.get()
    L.append(address)
    email=op_email.get
    L.append(email)
    phone=op_phone.get
    L.append(phone)
    value=L
    value=(op_id,name,address,email,phone)
    sql="insert into operator(op_id,name,address,email,phone)values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mydb.commit()
root=Tk()
root.title("Bus Booking")
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
bus=PhotoImage(file='.\\python_bus.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=w//2.5)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=15,padx=w//2.5,pady=h//20)
Label(root,text='Add Bus Operator Details',bg='floral white',fg='green3',font='Arial 16 bold').grid(row=2,column=0,columnspan=15)
Label(root,text='Operator id',fg='grey1',font='Arial 12').grid(row=3,column=0,pady=50)
o_id=Entry(root)
o_id.grid(row=3,column=1)
Label(root,text='Name',fg='grey1',font='Arial 12').grid(row=3,column=2)
op_name=Entry(root)
op_name.grid(row=3,column=3)
Label(root,text='Address',fg='grey1',font='Arial 12').grid(row=3,column=4)
op_address=Entry(root)
op_address.grid(row=3,column=5)
Label(root,text='Phone',fg='grey1',font='Arial 12').grid(row=3,column=6)
op_email=Entry(root)
op_email.grid(row=3,column=7)
Label(root,text='Email',fg='grey1',font='Arial 12').grid(row=3,column=8)
op_phone=Entry(root)
op_phone.grid(row=3,column=9)
Button(root,text='Add',bg='lawn green',fg='grey1',command=operatoradd).grid(row=3,column=10,padx=10)
Button(root,text='Edit',bg='lawn green',fg='grey1').grid(row=3,column=11,padx=10)
home=PhotoImage(file='.\\home.png')
Button(root,image=home).grid(row=4,column=8)
root.mainloop()

