import mysql.connector
from tkinter import *
from tkinter.messagebox import *
from datetime import date
tdate=date.today()
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             #passwd="Enter your mySQL Password Here",\
                             database="bus_booking")

mycursor=mydb.cursor()

class test:
    
    def addrun(self):
        def gohome():
            root.destroy()
            self.home()
        root=Tk()
        root.title('ADD RUNS')
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        bus=PhotoImage(file='.\\python_bus.png')
        Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Add Bus Running Details',bg='floral white',fg='green3',font='Arial 16 bold').grid(row=2,column=0,pady=20,columnspan=15)
        Label(root,text='Bus ID',fg='grey1',font='Arial 12').grid(row=3,column=0,pady=50)
        bus_id=Entry(root)
        bus_id.grid(row=3,column=1,padx=50)
        Label(root,text='Running Date',fg='grey1',font='Arial 12').grid(row=3,column=2)
        date=Entry(root)
        date.grid(row=3,column=3,padx=50)
        Label(root,text='Seat Available',fg='grey1',font='Arial 12').grid(row=3,column=4)
        seat_avail=Entry(root)
        seat_avail.grid(row=3,column=5,padx=50)
        def pop1():
            showinfo('Runs Entry','Runs record added')
        def pop2():
            showerror('Runs Entry Update','Runs record deleted successfully')
        
        
        def run_data():
            try:
                mycursor.execute('insert into runs values({},"{}",{})'.format( bus_id.get(),date.get(),seat_avail.get()) )   
                mydb.commit()
                pop1()
            except:
                showerror("ERROR","Bus already running on given date")
        def run_delete():
            mycursor.execute('delete from runs  where bus_id={},date={}'.format(bus_id.get(),date.get()))
            mydb.commit()
            pop2()
        Button(root,text='Add Run',bg='lawn green',fg='grey1',command=run_data).grid(row=3,column=6,pady=20,padx=10)
        Button(root,text='Delete Run',bg='lawn green',fg='grey1',command=run_delete).grid(row=3,column=7,pady=20,padx=10)
        home=PhotoImage(file='.\\home.png')
        Button(root,image=home,command=gohome).grid(row=4,column=6)
        root.mainloop()
        


    def addroute(self):
        def gohome():
            root.destroy()
            self.home()
        root=Tk()
        root.title('ADD ROUTE')
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        bus=PhotoImage(file='.\\python_bus.png')
        Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Add Bus Route Details',bg='floral white',fg='green3',font='Arial 16 bold').grid(row=2,column=0,pady=20,columnspan=15)
        Label(root,text='Route Id',fg='grey1',font='Arial 12').grid(row=3,column=0,pady=50)
        route_id=Entry(root)
        route_id.grid(row=3,column=1,padx=50)
        Label(root,text='Station Id',fg='grey1',font='Arial 12').grid(row=3,column=4)
        s_id=Entry(root)
        s_id.grid(row=3,column=5,padx=50)
        Label(root,text='Station Name',fg='grey1',font='Arial 12').grid(row=3,column=2)
        s_name=Entry(root)
        s_name.grid(row=3,column=3,padx=50)
        def pop1():
            showinfo('Route Entry','Route record added')
        def pop2():
            showerror('Route Entry Update','Route record deleted successfully')
        
        
        def route_data():
            try:
                mycursor.execute('insert into route values({},{},"{}")'.format( route_id.get(),s_id.get(),s_name.get()) )   
                mydb.commit()
                pop1()
            except:
                showerror('ERROR','Route already exists')

        def route_delete():
            mycursor.execute('delete from route where route_id={}'.format(route_id.get()))
            mydb.commit()
            pop2()
        Button(root,text='Add Route',bg='lawn green',fg='grey1',command=route_data).grid(row=3,column=6,pady=20,padx=10)
        Button(root,text='Delete Route',bg='lawn green',fg='red',command=route_delete).grid(row=3,column=7,pady=20,padx=10)
        home=PhotoImage(file='.\\home.png')
        Button(root,image=home,command=gohome).grid(row=4,column=4)
        root.mainloop()


    
    def addbus(self):
        def gohome():
            root.destroy()
            self.home()
        
        root=Tk()
        root.title("ADD BUS")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        bus=PhotoImage(file='.\\python_bus.png')
        Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Add Bus Details',bg='floral white',fg='green3',font='Arial 16 bold').grid(row=2,column=0,pady=20,columnspan=15,padx=w//2.5)
        Label(root,text='Bus ID',fg='grey1',font='Arial 12').grid(row=3,column=0,pady=50)
        bus_id=Entry(root)
        bus_id.grid(row=3,column=1)
        bus_type=StringVar()
        option=("AC 2X2","AC 3X2","Non AC 2X2","Non AC 3X2","AC-Sleeper 2X1","Non-AC Sleeper 2X1")
        menu=OptionMenu(root,bus_type,*option)
        menu.grid(row=3,column=3)
        bus_type.set("Select Bus Type")
        Label(root,text='Bus Type',fg='grey1',font='Arial 12').grid(row=3,column=2)
        Label(root,text='Capacity',fg='grey1',font='Arial 12').grid(row=3,column=4)
        seating_capacity=Entry(root)
        seating_capacity.grid(row=3,column=5)
        Label(root,text='Fare Rs',fg='grey1',font='Arial 12').grid(row=3,column=6)
        fare=Entry(root)
        fare.grid(row=3,column=7)
        Label(root,text='Operator ID',fg='grey1',font='Arial 12').grid(row=3,column=8)
        op_id=Entry(root)
        op_id.grid(row=3,column=9)
        Label(root,text='Route id',fg='grey1',font='Arial 12').grid(row=3,column=10)
        route_id=Entry(root)
        route_id.grid(row=3,column=11)
        def pop1():
            showinfo('Bus Entry','Bus record added')
        def pop2():
            showinfo('Bus Entry Update','Bus record updated successfully')
        
        def bus_data():
            try:
                mycursor.execute('insert into bus values({},"{}",{},{},{},{})'.format( bus_id.get(),bus_type.get(),seating_capacity.get(),fare.get(),op_id.get(),route_id.get()) )   
                mydb.commit()
                pop1()
            except:
                showerror('ERROR','Operator ID already exists')
        def bus_update():
            mycursor.execute('update bus set type="{}",seating_capacity={},fare={},op_id={},route_id={} where bus_id={}'.format(bus_type.get(),seating_capacity.get(),fare.get(),op_id.get(),route_id.get(),bus_id.get()))
            mydb.commit()
            pop2()
        Button(root,text='Add Bus',bg='lawn green',fg='grey1',command=bus_data).grid(row=5,column=4,pady=20,columnspan=4)
        Button(root,text='Edit Bus',bg='lawn green',fg='grey1',command=bus_update).grid(row=5,column=5,pady=20,columnspan=4)
        home=PhotoImage(file='.\\home.png')
        Button(root,image=home,command=gohome).grid(row=5,column=6,columnspan=3)
        root.mainloop()

    
    def addoperator(self):
        def gohome():
            root.destroy()
            self.home()
        root=Tk()
        root.title("ADD OPERATOR")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        bus=PhotoImage(file='.\\python_bus.png')
        Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=15,padx=w//2.5,pady=h//20)
        Label(root,text='Add Bus Operator Details',bg='floral white',fg='green3',font='Arial 16 bold').grid(row=2,column=0,columnspan=15)
        Label(root,text='Operator id',fg='grey1',font='Arial 12').grid(row=3,column=0,pady=50)
        op_id=Entry(root)
        op_id.grid(row=3,column=1)
        Label(root,text='Name',fg='grey1',font='Arial 12').grid(row=3,column=2)
        name=Entry(root)
        name.grid(row=3,column=3)
        Label(root,text='Address',fg='grey1',font='Arial 12').grid(row=3,column=4)
        address=Entry(root)
        address.grid(row=3,column=5)
        Label(root,text='Email',fg='grey1',font='Arial 12').grid(row=3,column=6)
        email=Entry(root)
        email.grid(row=3,column=7)
        Label(root,text='Phone',fg='grey1',font='Arial 12').grid(row=3,column=8)
        phone=Entry(root)
        phone.grid(row=3,column=9)
        
        def pop1():
            showinfo('Operator Entry','Operator record added')
        def pop2():
            showinfo('Operator Entry Update','Operator record updated successfully')
        
        
        def save_data():
            try:
                mycursor.execute('insert into operator values({},"{}","{}","{}",{})'.format( op_id.get(),name.get(),address.get(),email.get(),phone.get()) )   
                mydb.commit()
                pop1()
            except:
                showerror('ERROR','Operator ID already exists')
           
                
        def update_data():
            mycursor.execute('update operator set name="{}",address="{}",email="{}",phone={} where op_id={}'.format(name.get(),address.get(),email.get(),phone.get(),op_id.get()))
            mydb.commit()
            pop2()
        
        Button(root,text='Add',bg='lawn green',fg='grey1',command=save_data).grid(row=3,column=10,padx=10)
        Button(root,text='Edit',bg='lawn green',fg='grey1',command=update_data).grid(row=3,column=11,padx=10)
        home=PhotoImage(file='.\\home.png')
        Button(root,image=home,command=gohome).grid(row=4,column=8)
        root.mainloop()
    


    def addnewdetails_home(self):
        root=Tk()
        root.title("ADD DETAILS")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        bus=PhotoImage(file='.\\python_bus.png')
        Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//2.5)
        Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=10,padx=w//2.5,pady=h//30)
        Label(root,text='Add New Details to DataBase',bg='floral white',fg='green3',font='Arial 16 bold').grid(row=2,column=0,columnspan=10,padx=w//2.5,pady=h//20)
        def add_operator():
            root.destroy()
            self.addoperator()
        def add_bus():
            root.destroy()
            self.addbus()
        def add_route():
            root.destroy()
            self.addroute()
        def add_run():
            root.destroy()
            self.addrun()
        Button(root,text='New Operator',bg='lawn green',fg='grey1',font='Arial 16',command=add_operator).grid(row=3,column=2)
        Button(root,text='New Bus',bg='orange red',fg='grey1',font='Arial 16 ',command=add_bus).grid(row=3,column=3)
        Button(root,text='New Route',bg='royal blue',fg='grey1',font='Arial 16 ',command=add_route).grid(row=3,column=4)
        Button(root,text='New Run',bg='light pink3',fg='grey1',font='Arial 16 ',command=add_run).grid(row=3,column=5) 
        root.mainloop()


    def seatcheck(self):
        root=Tk()
        root.title('SEAT CHECK')
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        bus=PhotoImage(file='.\\python_bus.png')
        Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Check Your Booking',fg='dark green',bg='green2',font='Arial 18 bold').grid(row=3,column=0,pady=20,columnspan=15)
        Label(root,text='Enter Your Mobile No:',fg='grey1',font='Arial 12').grid(row=4,column=5)
        mob=Entry(root)
        mob.grid(row=4,column=6)
        
        def gentkt():
            mobile=mob.get()
            if len(mobile)==10 and mobile.isdigit():    
                mycursor.execute('select * from booking_history where phone={}'.format(mobile))
                tkt_result=mycursor.fetchall()
                mydb.commit
                for i in tkt_result:
                    book_id=i[0]
                    name=i[1]
                    b_id=i[2]
                    d_booking=i[3]
                    d_travel=i[4]
                    seat=i[5]
                    sex=i[6]
                    phone_no=i[7]
                    age=i[8]
                mycursor.execute('select fare,route_id from bus where bus_id={}'.format(b_id))
                rec_bus=mycursor.fetchall()
                fare=rec_bus[0][0]
                route_id=rec_bus[0][1]
                
                mycursor.execute('select booking_id from booking_history where phone={}'.format(phone_no))
                rec_bk_h=mycursor.fetchall()
                b_rec=rec_bk_h[0][0]
                box=Frame(root,borderwidth=5,relief='ridge')
                box.grid(row=5,column=6,pady=h//30)
                Label(box,text="YOUR TICKET", font='Arial 12 bold',fg='grey1').pack()
                Label(box,text="Booking ID : {}".format(b_rec),font='Arial 12 bold', fg='grey1').pack()
                Label(box,text="Name :" + name, font='Arial 12 bold', fg='grey1').pack()
                Label(box,text="Gender : " + sex, font='Arial 12 bold', fg='grey1').pack()
                Label(box,text="Seats Booked : " + str(seat), font='Arial 12 bold', fg='grey1').pack()
                Label(box,text="Age : " + str(age), font='Arial 12 bold', fg='grey1').pack()
                Label(box,text="Booked On :  {}".format(d_booking), font='Arial 12 bold', fg='grey1').pack()
                Label(box,text="Travel Date : {} ".format(d_travel), font='Arial 12 bold', fg='grey1').pack()
                Label(box,text="Fare :  " + str(fare), font='Arial 12 bold', fg='grey1').pack()
                Label(box,text="Total Fare :  " + str(fare*seat), font='Arial 12 bold', fg='grey1').pack()
            else:
                showerror("ERROR","Invalid Input")
        Button(root,text='Check Booking',command=gentkt).grid(row=4,column=7)
        root.mainloop()



    def busticket(self):
        root=Tk()
        root.title('BUS TICKET')
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        bus=PhotoImage(file='.\\python_bus.png')
        Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=15,padx=w//2.5,pady=h//20)
        Label(root,text='Bus Ticket',fg='grey1',font='Arial 16 bold').grid(row=2,column=0,columnspan=15,padx=w//2.5)
        box=Frame(root,borderwidth=5,relief='ridge')
        box.grid(row=4,column=7,pady=h//30)
        showinfo('Success','Seat Booked..')
        root.mainloop()
        



    def seatbooking(self):
        def gohome():
            root.destroy()
            self.home()
        root=Tk()
        root.title('SEAT BOOKING')
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        def show():
            def proceedbook():
                frame2=Frame(root)
                frame2.grid(row=7,column=0,columnspan=20,pady=h//30)
                Label(frame2,text='Fill Passenger Detail to book the bus ticket',bg='lightblue',fg='red',font='Arial 16 bold').grid(row=6,column=0,columnspan=20,padx=w//2.5,pady=h//30)
                Label(frame2,text='Name',font='Arial 12 bold').grid(row=8,column=1)
                name=Entry(frame2)
                name.grid(row=8,column=2)
                Label(frame2,text='Gender',font='Arial 12 bold').grid(row=8,column=3)
                gender=StringVar()
                gender.set('Male')
                option=('Male','Female')
                menu=OptionMenu(frame2,gender,*option)
                menu.grid(row=8,column=4)
                Label(frame2,text='No of Seats',font='Arial 12 bold').grid(row=8,column=5)
                seat_book=Entry(frame2)
                seat_book.grid(row=8,column=6)
                Label(frame2,text='Mobile No',font='Arial 12 bold').grid(row=8,column=7)
                phone=Entry(frame2)
                phone.grid(row=8,column=8)
                Label(frame2,text='Age',font='Arial 12 bold').grid(row=8,column=9)
                age=Entry(frame2)
                age.grid(row=8,column=10)
                def book_seat():
                    if (len(phone.get())!=10):
                        showerror("Error", message="Invalid Phone number")
                    else:
                        mycursor.execute("select seat_avail from runs where bus_id={} and date='{}'".format(bus_select.get(),c.get()))
                        seat_avail=mycursor.fetchall()
                        seat_avail=seat_avail[0][0]
                        if int(seat_book.get())<seat_avail:
                            mycursor.execute('insert into booking_history (person_name,bus_id,date_of_booking,date_of_travel,no_of_seat,gender,phone,age)values("{}",{},"{}","{}",{},"{}",{},{})'.format( name.get(),bus_select.get(),tdate,c.get(),seat_book.get(),gender.get(),phone.get(),age.get()) )
                            mycursor.execute("update runs set seat_avail=seat_avail-{} where BUS_ID={} and DATE='{}'".format(seat_book.get(), bus_select.get(),c.get()))
                            mydb.commit()
                        else:
                            showerror("Error", message="Invalid number of seats")
            
                def pop():
                    mycursor.execute("Select fare from bus where bus_id={}".format(bus_select.get()))
                    fare=mycursor.fetchall()
                    fare=fare[0][0]
                    choice=askyesnocancel('Fare Confirm','Total Amount to be paid Rs {}'.format(fare*int(seat_book.get())))
                    if choice==True:
                        book_seat()
                        root.destroy()
                        # self.busticket()
                        self.seatcheck()
                    
                button1=Button(frame2,text='Book Seat',font='Arial 12 bold',bg='lightgreen',command=pop)
                button1.grid(row=8,column=11)
                
            frame1=Frame(root)
            frame1.grid(row=4,column=0,columnspan=20,pady=h//30)
            Label(frame1,text='Select Bus',font='Arial 12 bold',fg='green').grid(row=4,column=2,padx=30)
            Label(frame1,text='Operator',font='Arial 12 bold',fg='green').grid(row=4,column=4,padx=30)
            Label(frame1,text='Bus Type',font='Arial 12 bold',fg='green').grid(row=4,column=6,padx=30)
            Label(frame1,text='AvailableCapacity',font='Arial 12 bold',fg='green').grid(row=4,column=8,padx=30)
            Label(frame1,text='Fare',font='Arial 12 bold',fg='green').grid(row=4,column=10,padx=30)
            mycursor.execute('''
                select op.name,b.type,r.seat_avail,b.fare,b.bus_id 
                from operator as op,runs as r,route as st,route as ed,bus as b 
                where st.s_name="{}"
                and ed.s_name="{}"
                and r.date="{}" 
                and b.bus_id=r.bus_id
                and  st.s_id<ed.s_id  
                and st.route_id=ed.route_id 
                and b.op_id=op.op_id
                and r.seat_avail>0
                and st.route_id=b.route_id;'''.format(a.get(),b.get(),c.get()))
            result=mycursor.fetchall()
            mydb.commit()
            bus_select=IntVar()
            i=0
            for i in range(len(result)):
                print(result[i][4])
                Radiobutton(frame1,text='Bus {}'.format(i+1),font='Arial 12 bold',fg='black',bg='lightblue',variable=bus_select,value=result[i][4]).grid(row=i+5,column=2)
                Label(frame1,text='{}'.format(result[i][0]),font='Arial 12  italic',fg='blue').grid(row=i+5,column=4)
                Label(frame1,text='{}'.format(result[i][1]),font='Arial 12 bold',fg='blue').grid(row=i+5,column=6)
                Label(frame1,text='{}'.format(result[i][2]),font='Arial 12 bold',fg='blue').grid(row=i+5,column=8)
                Label(frame1,text='{}'.format(result[i][3]),font='Arial 12 bold',fg='blue').grid(row=i+5,column=10)
            Button(root,text='Proceed to Book',font='Arial 12 bold',bg='lightgreen',command=proceedbook).grid(row=4,column=12)
        frame3=Frame(root)
        frame3.grid(row=3,column=0,columnspan=20,pady=h//30)
        bus=PhotoImage(file='.\\python_bus.png')
        Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Enter Journey Details',bg='green2',fg='dark green',font='Arial 16 bold').grid(row=2,column=0,columnspan=15,padx=w//2.5,pady=h//30)
        Label(frame3,text='To',fg='grey1',font='Arial 12').grid(row=3,column=2)
        a=Entry(frame3)
        a.grid(row=3,column=3)
        Label(frame3,text='From',fg='grey1',font='Arial 12').grid(row=3,column=4)
        b=Entry(frame3)
        b.grid(row=3,column=5)
        Label(frame3,text='Journey Date',fg='grey1',font='Arial 12').grid(row=3,column=6)
        c=Entry(frame3)
        c.grid(row=3,column=7)
        Button(frame3,text='Show Bus',bg='green3',command=show).grid(row=3,column=8)
        home=PhotoImage(file='.\\home.png')
        Button(root,image=home,command=gohome).grid(row=3,column=12)
        root.mainloop()



    def home(self):
        root=Tk()
        root.title("HOME")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        bus=PhotoImage(file='.\\python_bus.png')
        Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=w//2.5)
        Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=15,padx=w//2.5,pady=h//20)
        def seat_booking():
            root.destroy()
            self.seatbooking()
        def check_booking():
            root.destroy()
            self.seatcheck()
        def add_bus():
            root.destroy()
            self.addnewdetails_home()
        Button(root,text='Seat Booking',bg='green2',fg='grey1',font='Arial 16 bold',command=seat_booking).grid(row=4,column=4)
        Button(root,text='Check Booked Seat',bg='green3',fg='grey1',font='Arial 16 bold',command=check_booking).grid(row=4,column=6)
        Button(root,text='Add Bus Details',bg='dark green',fg='grey1',font='Arial 16 bold',command=add_bus).grid(row=4,column=8)
        Label(root,text='For Admin Only',fg='red',font='Arial 12 bold').grid(row=5,column=8)
        root.mainloop()


    def splitscreen(self):
        root=Tk()
        root.title('BUS BOOKING SYSTEM')
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        bus=PhotoImage(file='.\\python_bus.png')
        Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//2.5)
        Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,padx=w//2.5,pady=h//20)
        Label(root,text='Name: Akash Kumar',fg='blue',font='Arial 16 bold').grid(row=3,column=0,pady=h//80)
        Label(root,text='Er : 211B378',fg='blue',font='Arial 16 bold').grid(row=4,column=0,pady=h//80)
        Label(root,text='Mobile : 8318603271',fg='blue',font='Arial 16 bold').grid(row=5,column=0,pady=h//80)
        Label(root,text='Submitted To : Dr. Mahesh Kumar',bg='light blue',fg='red',font='Arial 20 bold').grid(row=8,column=0,pady=h//8)
        Label(root,text='ProjectBasedLearning',fg='red',font='Arial 16 bold').grid(row=9,column=0,pady=h//40)
        def close(e=1):
            root.destroy()
            self.home()
        root.bind("<KeyPress>",close)
        root.mainloop()
t=test()
t.splitscreen()
