#########################################################################################################
#########################################################################################################
#                                                                                                       #
#                                         ATM PROTOTYPE                                                 #
#                                                                                                       #
#########################################################################################################
#########################################################################################################


from tkinter import *
import time
root = Tk()
root.title("ATM MACHINE")
root.geometry("900x850")
root.configure(bg = "black")

f1 = Frame(root,bg="white",width=500, height=50, relief = SUNKEN)
f1.pack(side=TOP)

f2 = Frame(root,bg="black",width=400, height=700, relief = SUNKEN)
f2.pack(side=LEFT)

f3 = Frame(root,bg="black",width=300, height=700, relief = SUNKEN)
f3.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

l1 = Label(f1,font=('arial',30,'bold'), text="ATM MACHINE", fg="Powder Blue", bg="black", bd=10,anchor="w")
l1.grid(row=0,column=0)

l2 = Label(f1,font=('arial',20,'bold'), text=localtime, fg="Powder Blue", bg="black", bd=10,anchor="w")
l2.grid(row=1,column=0)


number = StringVar()
amount = StringVar()
withd = StringVar()
acca = " "


def bank():
    global acca
    accno = ['0009879','0001234','0009829','1002789','2030456']
    account = number.get()
    if account in accno:
        label.config(text = "Registered User")
        bank = {'0009879':10000,'0001234':20000,'0009829':30000}
        balance = bank[account]
        acca = balance
    else:
        label.config(text = "Non Registered User")

def deposit():
    global acca
    amo = float(amount.get())
    bal = acca+amo
    label3.config(text=("Net balance:",str(bal)))

def withdrawn():
    global acca
    wd = float(withd.get())
    if acca>=wd:
        ace = acca-wd
        label4.config(text=("Net balance :",str(ace)))
    else:
        label4.config(text="Insufficient Balance")

def bal():
    global area
    label5.config(text=("Net Balance",str(acca)))

def reset():
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")


        
l3 = Label(f2,font=('arial',16,'bold'), text = "Enter the account number        ",
fg="Powder Blue", bg="black",bd=10,anchor="w")
l3.grid(row=0,column=3)
txt = Entry(f2,font=('arial',16,'bold'), textvariable=number, bg="Powder Blue", 
bd=6, insertwidth=4, justify="right")
txt.grid(row=0,column=4)
label = Label(f2,font=('arial',16,'bold'), fg="white", bg="black")
label.grid(row=1,column=4)
btnsubmit = Button(f3,font=('arial',16,'bold'),padx=16,pady=4,bg="Powder Blue", fg="black", 
bd=10,width=7,text="SUBMIT",command=bank)
btnsubmit.grid(row=0,column=4)

l3Total = Label(f2,text="                            ",fg="white",bg="black")
l3Total.grid(row=3,columnspan=10)


l3 = Label(f2,font=('arial',16,'bold'), text = "Enter the amount to be deposited",
fg="Powder Blue", bg="black",bd=10,anchor="w")
l3.grid(row=4,column=3)
txt = Entry(f2,font=('arial',16,'bold'), textvariable=amount, bg="Powder Blue", 
bd=6, insertwidth=4, justify="right")
txt.grid(row=4,column=4)
label3 = Label(f2,font=('arial',16,'bold'), fg="white", bg="black")
label3.grid(row=5,column=5)
btndeposit = Button(f3,font=('arial',16,'bold'),padx=16,pady=4,bg="Powder Blue", fg="black", 
bd=10,width=7,text="DEPOSIT",command=bank)
btndeposit.grid(row=4,column=4)

l3Total = Label(f2,text="                            ",fg="white",bg="black")
l3Total.grid(row=7,columnspan=10)


l3 = Label(f2,font=('arial',16,'bold'), text = "Enter the amount to be withdrawn",
fg="Powder Blue", bg="black",bd=10,anchor="w")
l3.grid(row=8,column=3)
txt = Entry(f2,font=('arial',16,'bold'), textvariable=withd, bg="Powder Blue", 
bd=6, insertwidth=4, justify="right")
txt.grid(row=8,column=4)
label4 = Label(f2,font=('arial',16,'bold'), fg="white", bg="black")
label4.grid(row=9,column=4)
label5 = Label(f2,font=('arial',16,'bold'), fg="white", bg="black")
label5.grid(row=10,column=4)

btnwithdraw = Button(f3,font=('arial',16,'bold'),padx=16,pady=4,bg="Powder Blue", fg="black", 
bd=10,width=7,text="WITHDRAWL",command=withdrawn)
btnwithdraw.grid(row=8,column=4)
btnbal = Button(f3,font=('arial',16,'bold'),padx=16,pady=4,bg="Powder Blue", fg="black", 
bd=10,width=7,text="BALANCE",command=bal)
btnbal.grid(row=10,column=4)
btnreset = Button(f3,font=('arial',16,'bold'),padx=16,pady=4,bg="Powder Blue", fg="black", 
bd=10,width=7,text="RESET",command=reset)
btnreset.grid(row=11,column=4)
btnexit = Button(f3,font=('arial',16,'bold'),padx=16,pady=4,bg="Powder Blue", fg="black", 
bd=10,width=7,text="EXIT",command=root.destroy)
btnexit.grid(row=12,column=4)



root.mainloop()