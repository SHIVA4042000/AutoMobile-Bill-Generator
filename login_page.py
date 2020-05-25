from tkinter import *
import mysql.connector
import bill

root1 = Tk()
root1.resizable(False, False)
window_height = 350
window_width = 450
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root1.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def loginfn():
    conn = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
    cursor = conn.cursor()
    global label3
    global label4
    label3.destroy()
    label4.destroy()
    label3 = Label(frame1, text="Try Again!, Incorrect user ID and Password", bg=bg_color, fg="white")
    label4 = Label(frame1, text="Try Again!, Incorrect Password", bg=bg_color, fg="white")
    a = user_id_txt.get()
    b = password_txt.get()
    sql ="SELECT * from login where User_ID = %s;"
    cursor.execute(sql,(a,))
    result =cursor.fetchall()
    print(result)
    sql2 ="Select SHA1(%s) ;"
    cursor.execute(sql2,(b,))
    result2 =cursor.fetchall()
    if result == []:

        label3.place(x=110, y=250)
    else:
        if result[0][1] == a and result[0][2] != result2[0][0]:
            label4.place(x=130, y=250)
        elif result[0][1] == a and result[0][2]== result2[0][0]:

            root1.destroy()
            bill.root = Tk()
            obj = bill.Bill_App(bill.root)
            bill.root.mainloop()

    conn.close()
    cursor.close()


bg_color = "#027E2C"
frame =LabelFrame(root1,bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
frame.place(x=0,y=0,width=450,height=350)
title=Label(frame,text="SIGN IN",bd=8,relief=GROOVE,bg=bg_color,fg="white",font =("times new roman",20,"bold"),pady=2)
title.pack(fill=X)
frame1 =LabelFrame(frame,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
frame1.place(x=1,y=51,width=428,height=278)

label0=Label(frame1,text="   ",bg=bg_color).grid(row=0,column=0,pady=10)
user_id=Label(frame1,text="      USER ID",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
user_id.grid(row=1,column=0,padx=10,pady=10)
user_id_txt=Entry(frame1,width=16,font="arial 15",bd=7,relief=SUNKEN)
user_id_txt.grid(row=1,column=1,padx=10,pady=10)
bullet = "\u2022"
password=Label(frame1,text="      PASSWORD",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
password.grid(row=2,column=0,padx=10,pady=10)
password_txt=Entry(frame1,width=16,show=bullet,font="arial 15",bd=7,relief=SUNKEN)
password_txt.grid(row=2,column=1,padx=10,pady=10)

sign_in_btn =Button(frame1,text="SIGN IN",fg="white",font=("times new roman",15,"bold"),command=loginfn,bg=bg_color)
sign_in_btn.place(x=165,y=200)


label3 = Label(frame1)

label4 = Label(frame1)



root1.mainloop()