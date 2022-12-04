from tkinter import *
root=Tk()
root.title("Bus Booking")
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
bus=PhotoImage(file='.\\python_bus.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//2.5)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=10,padx=w//2.5,pady=h//30)
Label(root,text='Add New Details to DataBase',bg='floral white',fg='green3',font='Arial 16 bold').grid(row=2,column=0,columnspan=10,padx=w//2.5,pady=h//20)
Button(root,text='New Operator',bg='lawn green',fg='grey1',font='Arial 16').grid(row=3,column=2)
Button(root,text='New Bus',bg='orange red',fg='grey1',font='Arial 16 ').grid(row=3,column=3)
Button(root,text='New Route',bg='royal blue',fg='grey1',font='Arial 16 ').grid(row=3,column=4)
Button(root,text='New Run',bg='light pink3',fg='grey1',font='Arial 16 ').grid(row=3,column=5)
root.mainloop()