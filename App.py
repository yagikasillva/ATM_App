from tkinter import *
#from PIL import Image, ImageTk
from tkinter import messagebox,PhotoImage

global account_Balance
global account_detail

account_Balance = 250000
account_detail = ["Hakmeemana Kalukapuge Asantha Yagika Silva",account_Balance,"Debit Card","07501023023","199856478V"]
# create root window
root = Tk()
# root window title and dimension
root.title("HNB BANK")
root.iconbitmap('bank.ico')
# Set geometry(widthxheight)
root.geometry('450x300')
# adding a image
img =PhotoImage(file="bank.png")
image_label=Label(root,image=img)
image_label.pack()

lbl1 = Label(root, text="𝗛𝗲𝗹𝗹𝗼 𝗖𝘂𝘀𝘁𝗼𝗺𝗺𝗲𝗿 ",fg="black",font=("Helvetica",15))
lbl1.place(x=160, y=70)
lbl2 = Label(root, text="𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐭𝐞𝐫 𝐲𝐨𝐮𝐫 𝐏𝐈𝐍 𝐍𝐔𝐌𝐁𝐄𝐑",fg="black",font=("Georgia",15))
lbl2.place(x=110, y=100)
# adding Entry Field
txt = Entry(root, width=20,font=("Georgia",16),justify="center", bd=3,show='*')#bd = boarder, show is to hide
txt.place(x=90, y=150)
txt.delete(0, "end")


#error message display
def error_Message():
    messagebox.showerror("Error","𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝗮 𝘃𝗮𝗹𝗶𝗱 𝗣𝗜𝗡 𝗡𝘂𝗺𝗯𝗲𝗿")
def Herror_Message():
    messagebox.showerror("Error","𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗖𝗿𝗲𝗱𝗲𝗻𝘁𝗶𝗮𝗹𝘀. 𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻.")
    
# Function to create a new window
def home_page():
    new_window = Toplevel(root)
    new_window.title("HNB BANK - Main Menu")
    root.iconbitmap('bank.ico')
    new_window.geometry('450x300')

    heading = Label (new_window,text="•°o.O•°o.O 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗛𝗡𝗕 𝗕𝗮𝗻𝗸 O.o°•O.o°•\n𝗦𝗲𝗹𝗲𝗰𝘁 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗱𝗼",justify="center",font=("Helvetica",15),fg="#1964b1")
    heading.pack()
    
    main_menu_label1 = Label(new_window, text="𝟏. 𝐂𝐡𝐞𝐜𝐤 𝐁𝐚𝐥𝐚𝐧𝐜𝐞",justify="center",font=("Helvetica",13))
    main_menu_label1.pack()
    
    main_menu_label2 = Label(new_window, text="𝟐. 𝐃𝐞𝐩𝐨𝐬𝐢𝐭 𝐌𝐨𝐧𝐞𝐲",justify="center",font=("Helvetica",13))
    main_menu_label2.pack()
    
    main_menu_label3 = Label(new_window, text="𝟑. 𝐖𝐢𝐭𝐡𝐝𝐫𝐚𝐰 𝐌𝐨𝐧𝐞𝐲",justify="center",font=("Helvetica",13))
    main_menu_label3.pack()
    
    main_menu_label4 = Label(new_window, text="𝟒. 𝐓𝐫𝐚𝐧𝐬𝐟𝐞𝐫 𝐌𝐨𝐧𝐞𝐲",justify="center",font=("Helvetica",13))
    main_menu_label4.pack()
    
    main_menu_label5 = Label(new_window, text="𝟓. 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐃𝐞𝐭𝐚𝐢𝐥𝐬",justify="center",font=("Helvetica",13))
    main_menu_label5.pack()
    
    main_menu_label6 = Label(new_window, text="𝟔. 𝐁𝐚𝐜𝐤",justify="center",font=("Helvetica",13))
    main_menu_label6.pack()
    
    global input1 
    input1 = Entry(new_window, width=20,font=("Georgia",16),justify="center", bd=3)
    input1.pack()

    btn2 = Button(new_window, text="𝗢𝗞𝗔𝗬", fg="#fbdd0c", bg="#1966b5", command=home_Function,pady=5,padx=5)#DISTROY WILL CLOSE ONLY THE ONE WINDOW. qUIT CLOSE ALL WINDOWS.
    ##btn2.pack()
    btn2.pack()

#check Balace function
def check_balance(account_Balance):
    balance_window = Toplevel(root)
    balance_window.title("HNB BANK - Account Balance")
    root.iconbitmap('bank.ico')
    balance_window.geometry('400x180')
   
    
    heading = Label (balance_window,text="•°o.O•°o.O 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗛𝗡𝗕 𝗕𝗮𝗻𝗸 O.o°•O.o°•",justify="center",font=("Helvetica",15),fg="#1964b1")
    heading.pack()
    
    balance_print = Label (balance_window, text=f"Your Account Balance is ... \n{account_Balance}.00 LKR",font=('Helvetica', 12))
    balance_print.pack()
    
    backB = Button(balance_window, text="𝗕𝗔𝗖𝗞", fg="red", bg="#d9d9d9" ,command=balance_window.destroy,pady=5,padx=5)
    backB.pack()
    
    #backE= Button(balance_window, text="𝗘𝗫𝗜𝗧", fg="red", bg="#d9d9d9" ,command=balance_window.quit,pady=5,padx=5)
    #backE.pack()


#Main
def cash_Deposit(input1):
    cash_Deposit_window = Toplevel(root)
    cash_Deposit_window.title("HNB BANK ")
    root.iconbitmap('bank.ico')
    cash_Deposit_window.geometry('400x300')
    
    Mheading = Label (cash_Deposit_window,text="•°o.O•°o.O 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗛𝗡𝗕 𝗕𝗮𝗻𝗸 O.o°•O.o°•\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗮𝗺𝗼𝘂𝗻𝘁 𝗵𝗲𝗿𝗲",justify="center",font=("Helvetica",15),fg="#1964b1")
    Mheading.pack()
    
    deposit = Entry(cash_Deposit_window, width=20,font=("Georgia",16),justify="center", bd=3)
    deposit.pack()
    deposit.delete(0,END)
    
    if input1 == 3:
        buttonD2 = Button(cash_Deposit_window,text="𝗖𝗢𝗡𝗙𝗜𝗥𝗠",fg="#fbdd0c", bg="#1966b5" ,command=lambda: cash_Withdraw_Message(account_Balance,float(deposit.get())),pady=5,padx=5)#lamda is use when it have many functions and arguments in it
        buttonD2.place(x=100, y=100)
        backB = Button(cash_Deposit_window, text="𝗕𝗔𝗖𝗞", fg="red", bg="#d9d9d9" ,command=cash_Deposit_window.destroy,pady=5,padx=15)
        backB.place(x=220, y=100)
    elif input1 == 2:
        buttonD = Button(cash_Deposit_window,text="𝗖𝗢𝗡𝗙𝗜𝗥𝗠",fg="#fbdd0c", bg="#1966b5"  ,command=lambda: cash_Deposit_Message(account_Balance,float(deposit.get())),pady=5,padx=5)#lamda is use when it have many functions and arguments in it
        buttonD.place(x=100, y=100)
        backB = Button(cash_Deposit_window, text="𝗕𝗔𝗖𝗞", fg="red", bg="#d9d9d9" ,command=cash_Deposit_window.destroy,pady=5,padx=15)
        backB.place(x=220, y=100)
        
    
         
    #1st part
def cash_Deposit_Message(account_Balance,deposit):
    cash_Deposit_Message_window = Toplevel(root)
    cash_Deposit_Message_window.title("HNB BANK - Cash Deposit")
    root.iconbitmap('bank.ico')
    cash_Deposit_Message_window.geometry('400x300')
    
    #background color
    #cash_Deposit_Message_window.config(bg="#e6e6e6")
    
    account_Balance += deposit
    
    Fmessage = Label (cash_Deposit_Message_window,text=f"𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗗𝗲𝗽𝗼𝘀𝗶𝘁𝗲𝗱 𝘁𝗵𝗲 𝗔𝗺𝗼𝘂𝗻𝘁 {deposit:.2f} 𝗟𝗞𝗦",font=("Georgia",12),justify="center")
    Fmessage.place(x=20,y=25)
    
    Tmessage= Label(cash_Deposit_Message_window,text=f"𝗬𝗼𝘂𝗿 𝗕𝗮𝗹𝗮𝗰𝗲 𝗶𝘀 {account_Balance:.2f} 𝗟𝗞𝗦",font=("Georgia",13),justify="center" )
    Tmessage.place(x=90,y=55)
    
    backB = Button(cash_Deposit_Message_window, text="𝗕𝗔𝗖𝗞", fg="red", bg="#d9d9d9" ,command=cash_Deposit_Message_window.destroy,pady=5,padx=5)
    backB.place(x=170, y=120) 
def cash_Withdraw_Message(account_Balance,deposit):
    cash_Withdraw_Message_window = Toplevel(root)
    cash_Withdraw_Message_window.title("HNB BANK - Cash Withdraw")
    root.iconbitmap('bank.ico')
    cash_Withdraw_Message_window.geometry('400x300')
    
    #background color
    #cash_Withdraw_Message_window.config(bg="#e6e6e6")
    
    account_Balance -= deposit
    
    Fmessage = Label (cash_Withdraw_Message_window,text=f"𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗪𝗶𝘁𝗵𝗱𝗿𝗮𝘄 𝘁𝗵𝗲 𝗔𝗺𝗼𝘂𝗻𝘁 {deposit:.2f} 𝗟𝗞𝗦",font=("Georgia",12),justify="center")
    Fmessage.place(x=20,y=25)
    
    Tmessage= Label(cash_Withdraw_Message_window,text=f"𝗬𝗼𝘂𝗿 𝗕𝗮𝗹𝗮𝗰𝗲 𝗶𝘀 {account_Balance:.2f} 𝗟𝗞𝗦" ,font=("Georgia",13),justify="center")
    Tmessage.place(x=90,y=55)
    
    backB = Button(cash_Withdraw_Message_window, text="𝗕𝗔𝗖𝗞", fg="red", bg="#d9d9d9" ,command=cash_Withdraw_Message_window.destroy,pady=5,padx=5)
    backB.place(x=170, y=120)  
 
 
def cash_Transfer():
    cash_Transfer_window = Toplevel(root)
    cash_Transfer_window.title("HNB BANK ")
    root.iconbitmap('bank.ico')
    cash_Transfer_window.geometry('400x300')
    
    Mheading = Label (cash_Transfer_window,text="•°o.O•°o.O 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗛𝗡𝗕 𝗕𝗮𝗻𝗸 O.o°•O.o°•\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗮𝗺𝗼𝘂𝗻𝘁 𝗵𝗲𝗿𝗲",justify="center",font=("Helvetica",15),fg="#1964b1")
    Mheading.pack()
    
    deposit = Entry(cash_Transfer_window, width=20,font=("Georgia",16),justify="center", bd=3)
    deposit.pack()
    deposit.delete(0,END)
    
    sHeading = Label(cash_Transfer_window,text="𝗣𝗹𝗲𝗮𝘀𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝘁𝗵𝗲 𝗮𝗰𝗰𝗼𝘂𝗻𝘁 𝗻𝘂𝗺𝗯𝗲𝗿")
    sHeading.pack()
    
    accNumber = Entry(cash_Transfer_window, width=20,font=("Georgia",16),justify="center", bd=3)
    accNumber.pack()
    accNumber.delete(0,END)
    
    
    buttonD2 = Button(cash_Transfer_window,text="𝗖𝗢𝗡𝗙𝗜𝗥𝗠",fg="#fbdd0c", bg="#1966b5"  ,command=lambda: cash_Transfer_Message(account_Balance,float(deposit.get()),str(accNumber.get())),pady=5,padx=5)#lamda is use when it have many functions and arguments in it
    buttonD2.place(x=100, y=180)
    backB = Button(cash_Transfer_window, text="𝗕𝗔𝗖𝗞", fg="red", bg="#d9d9d9" ,command=cash_Transfer_window.destroy,pady=5,padx=15)
    backB.place(x=220, y=180)
def cash_Transfer_Message(account_Balance, deposit, accNumber):
    cash_Transfer_Message_window = Toplevel(root)
    cash_Transfer_Message_window.title("HNB BANK - Cash Transfer")
    root.iconbitmap('bank.ico')
    cash_Transfer_Message_window.geometry('400x300')
    
    #background color
    #cash_Withdraw_Message_window.config(bg="#e6e6e6")
    
    account_Balance -= deposit
    
    Fmessage = Label (cash_Transfer_Message_window,text=f"𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗪𝗶𝘁𝗵𝗱𝗿𝗮𝘄 𝘁𝗵𝗲 𝗔𝗺𝗼𝘂𝗻𝘁 {deposit:.2f} 𝗟𝗞𝗦\n𝘁𝗵𝗲 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗡𝘂𝗺𝗯𝗲𝗿 {accNumber}",font=("Georgia",12),justify="center",)
    Fmessage.place(x=14, y=30)
    
    Tmessage= Label(cash_Transfer_Message_window,text=f"𝗬𝗼𝘂𝗿 𝗕𝗮𝗹𝗮𝗰𝗲 𝗶𝘀 {account_Balance:.2f} 𝗟𝗞𝗦" ,font=("Georgia",13),justify="center",)
    Tmessage.place(x=80,y=80)
    
    backB = Button(cash_Transfer_Message_window, text="𝗕𝗔𝗖𝗞", fg="red", bg="#d9d9d9" ,command=cash_Transfer_Message_window.destroy,pady=5,padx=5)
    backB.place(x=170, y=120)    


def account_Info():
    root2= Toplevel(root)    
    root2.title("HNB BANK")
    root2.iconbitmap('bank.ico')
    # Set geometry(widthxheight)
    root2.geometry('450x300')
    
    
    heading = Label (root2,text="•°o.O•°o.O 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗛𝗡𝗕 𝗕𝗮𝗻𝗸 O.o°•O.o°•\n𝗦𝗲𝗹𝗲𝗰𝘁 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗱𝗼",justify="center",font=("Helvetica",15),fg="#1964b1")
    heading.pack()
        
    main_menu_label1 = Label(root2, text="𝟭. 𝗖𝗵𝗲𝗰𝗸 𝗔𝗯𝗼𝘂𝘁",justify="center",font=("Helvetica",13))
    main_menu_label1.pack()
    
    main_menu_label2 = Label(root2, text="𝟮.𝐁𝐚𝐜𝐤",justify="center",font=("Helvetica",13))
    main_menu_label2.pack()
    
    main_menu_label4 = Label(root2, text="  ",justify="center",font=("Helvetica",13))
    main_menu_label4.pack()
    
    global input1 
    input1 = Entry(root2, width=20,font=("Georgia",16),justify="center", bd=3)
    input1.pack()

    check_Info = Button(root2,text="Click",fg="#fbdd0c", bg="#1966b5" ,pady=5,padx=5,command=lambda: check(root2,int(input1.get())))
    check_Info.pack()
    
def check_About(account_detail):
    check_About=Toplevel(root)
    check_About.title("Check About")
    check_About.iconbitmap('bank.ico')
    check_About.geometry('450x300')
    
    main_menu_label1 = Label(check_About, text="𝟭. 𝗖𝗮𝗿𝗱𝗵𝗼𝗹𝗱𝗲𝗿 𝗡𝗮𝗺𝗲",justify="center",font=("Helvetica",13))
    main_menu_label1.pack()
    
    main_menu_label2 = Label(check_About, text="𝟮. 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗕𝗮𝗹𝗮𝗻𝗰𝗲",justify="center",font=("Helvetica",13))
    main_menu_label2.pack()
    
    main_menu_label3 = Label(check_About, text="𝟯. 𝗖𝗮𝗿𝗱 𝗧𝘆𝗽𝗲",justify="center",font=("Helvetica",13))
    main_menu_label3.pack()
    
    main_menu_label4 = Label(check_About, text="𝟰. 𝗧𝗲𝗹𝗲𝗽𝗵𝗼𝗻𝗲 𝗡𝘂𝗺𝗯𝗲𝗿",justify="center",font=("Helvetica",13))
    main_menu_label4.pack()
    
    main_menu_label5 = Label(check_About, text="𝟱. 𝗡𝗮𝘁𝗶𝗼𝗻𝗮𝗹 𝗜𝗱𝗲𝗻𝘁𝗶𝘁𝘆 𝗖𝗮𝗿𝗱 𝗡𝘂𝗺𝗯𝗲𝗿",justify="center",font=("Helvetica",13))
    main_menu_label5.pack()
    
    main_menu_label6 = Label(check_About, text="𝟲. 𝗠𝗮𝗶𝗻 𝗠𝗲𝗻𝘂",justify="center",font=("Helvetica",13))
    main_menu_label6.pack()
    
    global input1 
    input1 = Entry(check_About, width=20,font=("Georgia",16),justify="center", bd=3)
    input1.pack()
    
    def message_Display_window(name,display):
        card_holder_name_Message_window = Toplevel(root)
        card_holder_name_Message_window.title("HNB BANK - Cash Transfer")
        root.iconbitmap('bank.ico')
        card_holder_name_Message_window.geometry('400x300')
        Fmessage = Label (card_holder_name_Message_window,text=f"{display}",font=("Georgia",15,"bold"),justify="center",)
        Fmessage.pack(pady=20,padx=20)
        
        Fmessage = Label (card_holder_name_Message_window,text=f"{name}",font=("Arial",10),justify="center",)
        Fmessage.pack(padx=20)
        
        Tmessage= Label(card_holder_name_Message_window,text=f"𝗧𝗵𝗮𝗻𝗸 𝗬𝗼𝘂 𝗳𝗼𝗿 𝗕𝗮𝗻𝗸𝗶𝗻𝗴 𝘄𝗶𝘁𝗵 𝘂𝘀" ,font=("Georgia",13),justify="center",)
        Tmessage.pack(pady=20)
        
        backB = Button(card_holder_name_Message_window, text="𝗕𝗔𝗖𝗞", fg="red", bg="#d9d9d9" ,command=card_holder_name_Message_window.destroy,pady=5,padx=5)
        backB.pack(pady=20)         
    def check(account_detail,input1):
        if input1 == "1":
            name = account_detail[0]
            display = "Acount Holder Name : "
            message_Display_window(name,display)
        elif input1 == "2":
            name = account_detail[1]
            display = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗕𝗮𝗹𝗮𝗻𝗰𝗲 : "
            message_Display_window(name,display)
        elif input1 == "3":
            name = account_detail[2]
            display = "𝗖𝗮𝗿𝗱 𝗧𝘆𝗽𝗲 : "
            message_Display_window(name,display)
        elif input1 == "4":
            name = account_detail[3]
            display = "𝗧𝗲𝗹𝗲𝗽𝗵𝗼𝗻𝗲 𝗡𝘂𝗺𝗯𝗲𝗿 : "
            message_Display_window(name,display)
        elif input1 == "5":
            name = account_detail[4]
            display = "𝗡𝗮𝘁𝗶𝗼𝗻𝗮𝗹 𝗜𝗱𝗲𝗻𝘁𝗶𝘁𝘆 𝗖𝗮𝗿𝗱 𝗡𝘂𝗺𝗯𝗲𝗿 : "
            message_Display_window(name,display)
        elif input1 == "6":
            check_About.destroy()


    check_Info = Button(check_About,text="Click",fg="#fbdd0c", bg="#1966b5" ,pady=5,padx=5,command=lambda: check(account_detail,str(input1.get())))
    check_Info.pack()
    
       
def check(root2,input1):
    if input1 == 1:
        check_About(account_detail)
    elif input1 == 2:
        root2.destroy()
    else:
        Herror_Message()
#home fundtion
def home_Function():
    if len(input1.get()) == 0:
        Herror_Message()
    elif int(input1.get()) == 1:
        messagebox.askquestion("HNB BANK","𝗪𝗶𝘀𝗵 𝘁𝗼 𝗣𝗿𝗼𝗰𝗲𝗲𝗱")
        check_balance(account_Balance)
    elif int(input1.get()) == 2:
        messagebox.askquestion("HNB BANK","𝗪𝗶𝘀𝗵 𝘁𝗼 𝗣𝗿𝗼𝗰𝗲𝗲𝗱")
        cash_Deposit(int(input1.get()))
    elif int(input1.get()) == 3:
        messagebox.askquestion("HNB BANK","𝗪𝗶𝘀𝗵 𝘁𝗼 𝗣𝗿𝗼𝗰𝗲𝗲𝗱")
        cash_Deposit(int(input1.get()))
    elif int(input1.get()) == 4:
        messagebox.askquestion("HNB BANK","𝗪𝗶𝘀𝗵 𝘁𝗼 𝗣𝗿𝗼𝗰𝗲𝗲𝗱")
        cash_Transfer()
    elif int(input1.get()) == 5:
        messagebox.askquestion("HNB BANK","𝗪𝗶𝘀𝗵 𝘁𝗼 𝗣𝗿𝗼𝗰𝗲𝗲𝗱")
        account_Info()
    elif int(input1.get()) == 6:
        messagebox.askquestion("HNB BANK","𝗪𝗶𝘀𝗵 𝘁𝗼 𝗣𝗿𝗼𝗰𝗲𝗲𝗱")
        home_page().new_window.destroy()
    else:
        Herror_Message()


# function to display user text when
# button is clicked
def clicked():
    if len(txt.get()) == 4:
        # Open a new window when the button is clicked
        home_page()
    else:
        error_Message()
        

# button widget with red color text inside
btn = Button(root, text="𝗡𝗘𝗫𝗧", fg="#fbdd0c", bg="#1966b5" ,command=clicked,pady=5,padx=5)
# Set Button Grid
btn.place(x=195, y=200)


# Execute Tkinter
root.mainloop()
