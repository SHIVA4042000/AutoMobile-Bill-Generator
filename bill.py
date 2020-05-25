from tkinter import *
from tkinter.ttk import Combobox
# noinspection PyUnresolvedReferences
from tkinter.ttk import Notebook
# noinspection PyUnresolvedReferences
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import errors
import re
from tkinter import messagebox



class Bill_App:
      def __init__(self,root):
        self.root = root
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        #self.root.geometry("1366x768+0+0")
        self.root.title("Automobile Service Billing")
        bg_color = "#027E2C"
        title=Label(self.root,text="Automobile Service Billing",bd=12,relief=GROOVE,bg=bg_color,fg="white",font =("times new roman",30,"bold"),pady=2).pack(fill=X)




#varlable name=========
        #====================Customer Details================
        self.customer=StringVar()
        self.Phone =StringVar()

        #=====================Vehical Details================
        self.KM =StringVar()
        self.Class=StringVar()
        self.Brand=StringVar()
        self.model=StringVar()
        self.year=StringVar()
        self.colour=StringVar()
        self.fuel=StringVar()
        self.wheels=StringVar()
        self.cc=StringVar()
        self.gear=StringVar()
        self.power=StringVar()


        #=======================Job Card======================


        #====================Registration Search==============
        self.regsearch=StringVar()
        #====================Menu ===========================
        self.Totalpart =StringVar()
        self.TotalLabour =StringVar()
        self.GstLabour =StringVar()
        self.GstParts = StringVar()
        self.GrandTotal = StringVar()


        #============Customer Detail Frame
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        self.cname_txt=Entry(F1,width=16,state="readonly",textvariable=self.customer,font="arial 15",bd=7,relief=SUNKEN)
        self.cname_txt.grid(row=0,column=1,padx=5,pady=10)

        cphone_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        self.cphone_txt=Entry(F1,width=16,state="readonly",textvariable=self.Phone,font="arial 15",bd=7,relief=SUNKEN)
        self.cphone_txt.grid(row=0,column=3,padx=5,pady=10)

        caddress_lbl=Label(F1,text="Address",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        self.caddress_txt=Text(F1,width=52,font="arial 12",height=2,bd=7,relief=SUNKEN)
        self.caddress_txt.grid(row=0,column=5,padx=5)
        self.caddress_txt.config(state=DISABLED)


        #bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)


#========Vehical Details==

        F2 = Frame(self.root,bd=10, relief=GROOVE)
        bill_title1 = Label(F2, text="Vehical Details", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        F2.place(x=5, y=180, width=330, height=380)

        FF2 = Frame(F2, relief=GROOVE, bg=bg_color)
        # FF2.place(x=5, y=180, width=325, height=380)
        canvas = Canvas(FF2, bg=bg_color, width=290)
        scrollbar = Scrollbar(FF2, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg=bg_color, bd=2, relief=GROOVE)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        v=[]
        vclass_lbl = Label(scrollable_frame, text="Class", font=("times new roman", 16, "bold"), bg=bg_color,fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.vclass_txt = Combobox(scrollable_frame,state="disabled",textvariable=self.Class,values=v)
        self.vclass_txt.set("Select")
        self.vclass_txt.grid(row=0, column=1, padx=10, pady=10,ipady=5)
        self.vclass_txt.bind('<<ComboboxSelected>>',self.classvalues)

        vbrand_lbl = Label(scrollable_frame, text="Brand", font=("times new roman", 16, "bold"), bg=bg_color,fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.vbrand_txt = Combobox(scrollable_frame,state="disabled",textvariable=self.Brand,values=v)
        self.vbrand_txt.set("Select")
        self.vbrand_txt.grid(row=1, column=1, padx=10, pady=10,ipady=5)
        self.vbrand_txt.bind('<<ComboboxSelected>>',self.brandvalues)

        vmodel_lbl = Label(scrollable_frame, text="Model", font=("times new roman", 16, "bold"), bg=bg_color,fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.vmodel_txt = Combobox(scrollable_frame,state="disabled",textvariable=self.model,values=v)
        self.vmodel_txt.set("Select")
        self.vmodel_txt.grid(row=2, column=1, padx=10, pady=10,ipady=5)
        self.vmodel_txt.bind('<<ComboboxSelected>>', self.modelvalues)

        vyear_lbl = Label(scrollable_frame, text="Year", font=("times new roman", 16, "bold"), bg=bg_color,fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.vyear_txt = Combobox(scrollable_frame,state="disabled",textvariable=self.year,values=v)
        self.vyear_txt.set("Select")
        self.vyear_txt.grid(row=3, column=1, padx=10, pady=10,ipady=5)
        self.vyear_txt.bind('<<ComboboxSelected>>', self.yearvalues)

        vcolour_lbl = Label(scrollable_frame, text="Colour", font=("times new roman", 16, "bold"), bg=bg_color,fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.vcolour_txt = Combobox(scrollable_frame,state="disabled",textvariable=self.colour,values=v)
        self.vcolour_txt.set("Select")
        self.vcolour_txt.grid(row=4, column=1, padx=10, pady=10,ipady=5)
        self.vcolour_txt.bind('<<ComboboxSelected>>', self.colourvalues)

        vfuel_lbl = Label(scrollable_frame, text="Fuel", font=("times new roman", 16, "bold"), bg=bg_color,fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.vfuel_txt = Combobox(scrollable_frame,state="disabled",textvariable=self.fuel,values=v)
        self.vfuel_txt.set("Select")
        self.vfuel_txt.grid(row=5, column=1, padx=10, pady=10,ipady=5)
        self.vfuel_txt.bind('<<ComboboxSelected>>', self.fuelvalues)

        vwheels_lbl = Label(scrollable_frame, text="Wheels", font=("times new roman", 16, "bold"), bg=bg_color,fg="white").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.vwheels_txt = Combobox(scrollable_frame, state="disabled", textvariable=self.wheels, values=v)
        self.vwheels_txt.set("Select")
        self.vwheels_txt.grid(row=6, column=1, padx=10, pady=10,ipady=5)
        self.vwheels_txt.bind('<<ComboboxSelected>>', self.wheelsvalues)

        vcc_lbl = Label(scrollable_frame, text="CC", font=("times new roman", 16, "bold"), bg=bg_color,fg="white").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.vcc_txt = Combobox(scrollable_frame,state="disabled",textvariable=self.cc,values=v)
        self.vcc_txt.set("Select")
        self.vcc_txt.grid(row=7, column=1, padx=10, pady=10,ipady=5)
        self.vcc_txt.bind('<<ComboboxSelected>>', self.ccvalues)

        vgear_lbl = Label(scrollable_frame, text="Gear", font=("times new roman", 16, "bold"), bg=bg_color,fg="white").grid(row=8, column=0, padx=10, pady=10, sticky="w")
        self.vgear_txt = Combobox(scrollable_frame, state="disabled", textvariable=self.gear, values=v)
        self.vgear_txt.set("Select")
        self.vgear_txt.grid(row=8, column=1, padx=10, pady=10,ipady=5)
        self.vgear_txt.bind('<<ComboboxSelected>>', self.gearvalues)

        vpower_lbl = Label(scrollable_frame, text="Power(HP)", font=("times new roman", 16, "bold"), bg=bg_color,fg="white").grid(row=9, column=0, padx=10, pady=10, sticky="w")
        self.vpower_txt = Combobox(scrollable_frame,state="disabled",textvariable=self.power,values=v)
        self.vpower_txt.set("Select")
        self.vpower_txt.grid(row=9, column=1, padx=10, pady=10,ipady=5)


        FF2.place(x=1, y=40, height=320)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        scrollable_frame.place()



#========Job Card==
        F3 = Frame(self.root)
        F3.place(x=340, y=180, width=650, height=380)
        bill_title3 = Label(F3, text="Job Card", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        self.FF32 = LabelFrame(F3, bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        self.FF32.place(x=2, y=45, width=650, height=335)


        lable2 = Label(self.FF32,text="", bg=bg_color).grid(row=0, column=0)
        vkm_lbl = Label(self.FF32, text=" Total Km.     ", font=("times new roman", 15, "bold"), bg=bg_color,fg="white").grid(row=0, column=1, sticky="w")
        self.vkm_txt = Entry(self.FF32, textvariable=self.KM,state="readonly",font=("times new roman", 13, "bold"),width=10)
        self.vkm_txt.grid(row=0, column=2, ipady=6)

        lable2 = Label(self.FF32, text="        ", bg=bg_color).grid(row=0, column=3)

        self.test_list = []
        self.entry = Entry(self.FF32,font=("times new roman", 12, "bold"),width=20)
        self.entry.grid(row=0, column=4,ipady=6)
        self.entry.insert(0,"Search")
        self.entry.config(state="readonly")
        self.entry.bind('<Button-1>', self.listbox_show)
        self.entry.bind('<KeyRelease>', self.on_keyrelease)
        self.listbox = Listbox()
        self.cells7 = {}
        self.cells8 = {}
        self.cells9 = {(0, 0): Entry()}
        self.cells10 = {(0, 0): Entry()}

        lable1 = Label(self.FF32, text="JOBS PERFORMED:", font=("times new roman", 15, "bold"), fg="white",bg=bg_color).grid(row=1, column=0,ipady=0)


        lable2 = Label(self.FF32, bg=bg_color).grid(row=3, column=0)
        lable2 = Label(self.FF32, bg=bg_color).grid(row=4, column=0)
        lable2 = Label(self.FF32, bg=bg_color).grid(row=5, column=0)
        lable2 = Label(self.FF32, bg=bg_color).grid(row=6, column=0)
        lable2 = Label(self.FF32, bg=bg_color).grid(row=7, column=0)
        lable2 = Label(self.FF32, bg=bg_color).grid(row=8, column=0)
        lable2 = Label(self.FF32, bg=bg_color).grid(row=9, column=0)

        FF3 = Frame(self.FF32, relief=GROOVE, bg="white")
        # FF3.place(x=2, y=60, width=626, height=100)
        canvas1 = Canvas(FF3, bg=bg_color, width=200)
        scrollbar1 = Scrollbar(FF3, orient="vertical", command=canvas1.yview)
        self.scrollable_frame1 = Frame(canvas1, bg=bg_color, bd=5, relief=GROOVE, width=600)

        self.scrollable_frame1.bind(
            "<Configure>",
            lambda e: canvas1.configure(
                scrollregion=canvas1.bbox("all")
            )
        )

        canvas1.create_window((0, 0), window=self.scrollable_frame1, anchor="nw", width=610)
        canvas1.configure(yscrollcommand=scrollbar1.set)

        self.cells6 = {(0,0):Entry()}
        a1 = Label(self.scrollable_frame1, text="SNo.",bd=1,relief="solid", width=6).grid(row=0,column=0)
        a2 = Label(self.scrollable_frame1, text="Job Name",bd=1,relief="solid", width=53).grid(row=0, column=1)
        a3 = Label(self.scrollable_frame1, text="Hours",bd=1,relief="solid", width=8).grid(row=0, column=2)
        a4 = Label(self.scrollable_frame1, text="Rate",bd=1,relief="solid", width=8).grid(row=0, column=3)
        a5 = Label(self.scrollable_frame1, text="Amount",bd=1,relief="solid", width=8).grid(row=0, column=4)








        FF3.place(x=2, y=58, width=626, height=90)
        canvas1.pack(side="left", fill="both", expand=True)
        scrollbar1.pack(side="right", fill="y")
        self.scrollable_frame1.place()






        lable3 = Label(self.FF32, text="PARTS PURCHASED:", font=("times new roman", 15, "bold"), fg="white",bg=bg_color).grid(row=8, column=0)

        FFF3 = Frame(self.FF32, relief=GROOVE, bg="white")
        # FFF3.place(x=2, y=60, width=626, height=100)
        canvas2 = Canvas(FFF3, bg=bg_color, width=200)
        scrollbar2 = Scrollbar(FFF3, orient="vertical", command=canvas2.yview)
        self.scrollable_frame2 = Frame(canvas2, bg=bg_color, bd=5, relief=GROOVE, width=600)

        self.scrollable_frame2.bind(
            "<Configure>",
            lambda e: canvas2.configure(
                scrollregion=canvas2.bbox("all")
            )
        )

        canvas2.create_window((0, 0), window=self.scrollable_frame2, anchor="nw", width=610)
        canvas2.configure(yscrollcommand=scrollbar2.set)

        self.cells4 = {(0,0):Entry()}
        b1 = Label(self.scrollable_frame2, text="#Part", bd=1, relief="solid", width=6).grid(row=0, column=0)
        b2 = Label(self.scrollable_frame2, text="Part Name", bd=1, relief="solid", width=53).grid(row=0, column=1)
        b3 = Label(self.scrollable_frame2, text="Quant.", bd=1, relief="solid", width=8).grid(row=0, column=2)
        b4 = Label(self.scrollable_frame2, text="Rate", bd=1, relief="solid", width=8).grid(row=0, column=3)
        b5 = Label(self.scrollable_frame2, text="Amount", bd=1, relief="solid", width=8).grid(row=0, column=4)






        FFF3.place(x=2, y=192, width=626, height=125)
        canvas2.pack(side="left", fill="both", expand=True)
        scrollbar2.pack(side="right", fill="y")
        self.scrollable_frame2.place()



#Past Record==================

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1000, y=180, width=370, height=380)
        bill_title=Label(F5,text="Past Record",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        FF5=LabelFrame(F5,relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        FF5.pack(fill=BOTH,expand=1)


        Reg22_lbl = Label(FF5, text="Registration No.*", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid(row=0, column=0, padx=5, pady=10, sticky="w")
        self.Reg22_txt = Entry(FF5, width=16,textvariable=self.regsearch,font=("times new roman", 12, "bold"), bd=5,relief=SUNKEN)
        self.Reg22_txt.grid(row=0, column=1, padx=5, pady=10)


        self.iconPath = 'search5.jpg'
        self.icon = ImageTk.PhotoImage(Image.open(self.iconPath))
        self.icon_btn = Button(self.root,command=self.searchers, image=self.icon, width=20, height=20,border=0)
        self.icon_btn.place(x=1295,y=247)



        self.newcustomer =Button(FF5,text="Add New Customer",command=self.newcustomerf,state="disabled")
        self.newcustomer.grid(row=1,column=0)
        self.newjob =Button(FF5,text="Add New Job",command=self.newjobf,state="disabled")
        self.newjob.grid(row=1,column=1)







        FFF5 = Frame(FF5, relief=GROOVE, bg="white")
        # FF3.place(x=2, y=60, width=626, height=100)
        canvas4 = Canvas(FFF5, bg=bg_color, width=200)
        scrollbar4 = Scrollbar(FFF5, orient="vertical", command=canvas4.yview)
        self.scrollable_frame4 = Frame(canvas4, bg=bg_color, bd=5, relief=GROOVE)

        self.scrollable_frame4.bind(
            "<Configure>",
            lambda e: canvas4.configure(
                scrollregion=canvas4.bbox("all")
            )
        )

        canvas4.create_window((0, 0), window=self.scrollable_frame4, anchor="nw", width=325)
        canvas4.configure(yscrollcommand=scrollbar4.set)

        self.cells2 = {(0,0):Entry()}
        c1 = Label(self.scrollable_frame4,text="",bd=1,relief="solid",width=4,border=0,bg=bg_color)
        c1.grid(row=0,column=0,ipady=5)
        c2= Label(self.scrollable_frame4, text="Date",bd=1,relief="solid", width=10).grid(row=0, column=1, ipady=5)
        c3= Label(self.scrollable_frame4, text="Time",bd=1,relief="solid", width=9).grid(row=0, column=2, ipady=5)
        c4= Label(self.scrollable_frame4, text="#Invoice",bd=1,relief="solid", width=10).grid(row=0, column=3, ipady=5)
        c6= Label(self.scrollable_frame4, text="Total KM",bd=1,relief="solid", width=9).grid(row=0, column=4, ipady=5)














        '''height = 11
        width = 6
        cells = {}
        for i in range(height):  # Rows
          for j in range(width):  # Columns
              if i==0:
                  b = Entry(scrollable_frame4, text="", width=8)
                  b.grid(row=i, column=j, ipady=5)
                  cells[(i, j)] = b
                  if j == 0:
                      b = Entry(scrollable_frame4, text="", width=5)
                      b.grid(row=i, column=j, ipady=5)
                      cells[(i, j)] = b
              else:
                   b = Entry(scrollable_frame4, text="", width=8)
                   b.grid(row=i, column=j)
                   cells[(i, j)] = b'''






        FFF5.place(x=2, y=90, width=345, height=225)
        canvas4.pack(side="left", fill="both", expand=True)
        scrollbar4.pack(side="right", fill="y")
        self.scrollable_frame4.place()

#Menu Button Frame========

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl=Label(F6,text="Total Labour Charges", font=("times new roman", 14, "bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,font="arial 10 bold",state="readonly",textvariable=self.TotalLabour,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total Parts Charges", font=("times new roman", 14, "bold"), bg=bg_color,fg="white").grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, font="arial 10 bold",state="readonly",textvariable=self.Totalpart, bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Grand Total ", font=("times new roman", 14, "bold"), bg=bg_color,fg="white").grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, font="arial 10 bold",state="readonly",textvariable=self.GrandTotal, bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)



        c1_lbl = Label(F6, text="Labour's28% GST", font=("times new roman", 14, "bold"), bg=bg_color,fg="white").grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, font="arial 10 bold",state="readonly",textvariable=self.GstLabour, bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Part's 28% GST", font=("times new roman", 14, "bold"), bg=bg_color,fg="white").grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, font="arial 10 bold",state="readonly",textvariable=self.GstParts, bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        self.invoice_no1 =""

        btn_F=Frame(F6,bd=7,bg=bg_color,relief=GROOVE,pady=5)
        btn_F.place(x=750,width=580,height=105)

        save_btn=Button(btn_F,text="Save",bg="cadetblue",state="normal",fg="white",command=self.savebutton,pady=15,width=10,font="arial 15 bold",bd=2)
        save_btn.grid(row=0,column=0,padx=5,pady=5)
        self.Generate_btn = Button(btn_F, text="Generate Bill",state="disabled",command=self.generatebill, bg="cadetblue", fg="white", pady=15, width=10, font="arial 15 bold",bd=2)
        self.Generate_btn.grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear",command=self.clearall,bg="cadetblue", fg="white", pady=15, width=10, font="arial 15 bold",bd=2)
        Clear_btn.grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit", bg="cadetblue", fg="white",command=self.exitbutton, pady=15, width=10, font="arial 15 bold",bd=2)
        Exit_btn.grid(row=0, column=3, padx=5, pady=5)

      def searchers(self):
        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

          regg=self.regsearch.get()
          rex = re.compile("^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$")
          if rex.match(regg):
            print("Correct format")
            sql = "SELECT * FROM customer_details where Registration_No = %s ;"
            gerr = (regg ,)
            cursor.execute(sql, gerr)
            myresult = cursor.fetchall()
            Regsql=""
            vehsql=""

            for x in myresult:
              Regsql =x[1]
              self.customer.set(x[2])
              self.Phone.set(x[3])
              self.caddress_txt.config(state=NORMAL)
              self.caddress_txt.delete(1.0, END)
              self.caddress_txt.insert(END,x[4])
              self.caddress_txt.config(state=DISABLED)
              vehsql=x[5]
            if self.regsearch.get() != Regsql:
              self.customer.set("No Record Found")
              self.Phone.set("")
              self.caddress_txt.config(state=NORMAL)
              self.caddress_txt.delete(1.0,END)
              self.caddress_txt.config(state=DISABLED)
              self.newcustomer.config(state="normal")
              self.newjob.config(state="disabled")


            if self.regsearch.get() == Regsql:
              sql1 = "SELECT * FROM marketed_vehical where S_No = %s ;"
              gerr1 = (vehsql ,)
              cursor.execute(sql1, gerr1)
              myresult1 = cursor.fetchall()
              self.newjob.config(state="normal")
              self.newcustomer.config(state="disabled")
              for y in myresult1:
                self.Class.set(y[1])
                self.Brand.set(y[2])
                self.model.set(y[3])
                self.year.set(y[4])
                self.colour.set(y[5])
                self.fuel.set(y[6])
                self.wheels.set(y[7])
                self.cc.set(y[8])
                self.gear.set(y[9])
                self.power.set(y[10])
              sql2 = "SELECT * FROM job_card where Registration_No = %s ;"
              jobb1 =(Regsql ,)
              cursor.execute(sql2, jobb1)
              myresult2 = cursor.fetchall()
              cells1 = {}
              i1 = 0
              for r in myresult2:
                cells1[i1] = (myresult2[i1])
                i1 += 1
              print(cells1)

              draww =len(cells1)+1
              vaa = IntVar()
              for cellsv in range (1,draww):
                ins = cellsv - 1
                self.cells2[cellsv,0] = Radiobutton(self.scrollable_frame4, text="", variable=vaa,command=lambda: changeButton(vaa.get()), value=cellsv)
                self.cells2[cellsv,0].grid(row=cellsv, column=0, ipady=3, pady=1)

                self.cells2[cellsv, 1] = Entry(self.scrollable_frame4, text="", width=11)
                self.cells2[cellsv,1].grid(row=cellsv, column=1, ipady=5, ipadx=2)
                self.cells2[cellsv,1].insert(0,cells1[ins][7])
                self.cells2[cellsv,1].config(state="readonly")

                self.cells2[cellsv,2] = Entry(self.scrollable_frame4, text="", width=10)
                self.cells2[cellsv,2].grid(row=cellsv, column=2, ipady=5, ipadx=2)
                self.cells2[cellsv,2].insert(0,cells1[ins][8])
                self.cells2[cellsv,2].config(state="readonly")

                self.cells2[cellsv,3] = Entry(self.scrollable_frame4, text="", width=11)
                self.cells2[cellsv,3].grid(row=cellsv, column=3, ipady=5, ipadx=2)
                self.cells2[cellsv,3].insert(0,cells1[ins][6])
                self.cells2[cellsv,3].config(state="readonly")

                self.cells2[cellsv,4] = Entry(self.scrollable_frame4, text="", width=11)
                self.cells2[cellsv,4].grid(row=cellsv, column=4, ipady=5)
                self.cells2[cellsv,4].insert(0,cells1[ins][2])
                self.cells2[cellsv,4].config(state="readonly")

              print(self.cells2)
#view RadioButton
              def viewclick(value):

                try:
                  connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
                  if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    cursor = connection.cursor()
                    cursor.execute("select database();")
                    record = cursor.fetchone()
                    print("You're connected to database: ", record)
                  fg = value-1
                  partsT=cells1[fg][3]
                  quantity=cells1[fg][5]
#for parts
                  list200 =[]
                  first0 = 0
                  jaa = ","

                  for iaa in partsT:
                    if jaa in iaa:
                      yaa = partsT.index(jaa, first0)
                      list200.append(partsT[first0:yaa])
                      first0 = yaa + 1
#for quantity
                  list300 = []
                  first1 = 0
                  jaa1 = ","

                  for iaa1 in quantity:
                    if jaa1 in iaa1:
                      yaa1 = quantity.index(jaa1, first1)
                      list300.append(quantity[first1:yaa1])
                      first1 = yaa1 + 1


                  incr =0
                  cells3 = {}
                  for l00 in list200:
                    sql3 = "SELECT * FROM scooter_parts where S_No = %s ;"
                    cursor.execute(sql3, (l00 ,))
                    myresult3 = cursor.fetchall()
                    cells3[incr] =myresult3
                    incr += 1
                  print(cells3)
                  sizz = len(cells3)+1

                  grnd0 =0
                  for sizz0 in range(1,sizz):
                    inc1 = sizz0 - 1
                    self.cells4[sizz0,0] = Entry(self.scrollable_frame2, width=7)
                    self.cells4[sizz0,0].grid(row=sizz0, column=0)
                    self.cells4[sizz0,0].insert(0,cells3[inc1][0][1])
                    self.cells4[sizz0,0].config(state="readonly")

                    self.cells4[sizz0,1] = Entry(self.scrollable_frame2, width=62)
                    self.cells4[sizz0,1].grid(row=sizz0, column=1)
                    self.cells4[sizz0,1].insert(0,cells3[inc1][0][3])
                    self.cells4[sizz0,1].config(state="readonly")

                    self.cells4[sizz0,2] = Entry(self.scrollable_frame2, width=9)
                    self.cells4[sizz0,2].grid(row=sizz0, column=2)
                    self.cells4[sizz0,2].insert(0,list300[inc1])
                    self.cells4[sizz0,2].config(state="readonly")

                    self.cells4[sizz0,3] = Entry(self.scrollable_frame2, width=9)
                    self.cells4[sizz0,3].grid(row=sizz0, column=3)
                    self.cells4[sizz0,3].insert(0,cells3[inc1][0][4])
                    self.cells4[sizz0,3].config(state="readonly")

                    self.cells4[sizz0,4] = Entry(self.scrollable_frame2, width=9)
                    self.cells4[sizz0,4].grid(row=sizz0, column=4)
                    amount1 = float(self.cells4[sizz0,2].get())
                    amount2 = float(self.cells4[sizz0,3].get())
                    total0 = amount1*amount2
                    self.cells4[sizz0,4].insert(0,total0)
                    self.cells4[sizz0,4].config(state="readonly")
                    grnd0 = grnd0 + total0
#for Job Performed
                  JobP = cells1[fg][9]
                  HourH = cells1[fg][4]

                  #for Job Name
                  list400 = []
                  first2 = 0
                  jaa2 = ","

                  for iaa2 in JobP:
                    if jaa2 in iaa2:
                      yaa2 = JobP.index(jaa2, first2)
                      list400.append(JobP[first2:yaa2])
                      first2 = yaa2 + 1
                  # for Hour
                  list500 = []
                  first3 = 0
                  jaa3 = ","

                  for iaa3 in HourH:
                    if jaa3 in iaa3:
                      yaa3 = HourH.index(jaa3, first3)
                      list500.append(HourH[first3:yaa3])
                      first3 = yaa3 + 1

                  incr3 = 0
                  cells5 = {}
                  for l100 in list400:
                    sql4 = "SELECT * FROM job_performed where S_No = %s ;"
                    cursor.execute(sql4, (l100,))
                    myresult5 = cursor.fetchall()
                    cells5[incr3] = myresult5
                    incr3 += 1
                  print(cells5)
                  sizzzz = len(cells5) + 1

                  grnd1 =0
                  for sizz3 in range(1, sizzzz):
                    inc3 = sizz3 - 1
                    self.cells6[sizz3, 0] = Entry(self.scrollable_frame1, width=7)
                    self.cells6[sizz3, 0].grid(row=sizz3, column=0)
                    self.cells6[sizz3, 0].insert(0, cells5[inc3][0][0])
                    self.cells6[sizz3, 0].config(state="readonly")

                    self.cells6[sizz3, 1] = Entry(self.scrollable_frame1, width=62)
                    self.cells6[sizz3, 1].grid(row=sizz3, column=1)
                    self.cells6[sizz3, 1].insert(0, cells5[inc3][0][1])
                    self.cells6[sizz3, 1].config(state="readonly")

                    self.cells6[sizz3, 2] = Entry(self.scrollable_frame1, width=9)
                    self.cells6[sizz3, 2].grid(row=sizz3, column=2)
                    self.cells6[sizz3, 2].insert(0, list500[inc3])
                    self.cells6[sizz3, 2].config(state="readonly")

                    self.cells6[sizz3, 3] = Entry(self.scrollable_frame1, width=9)
                    self.cells6[sizz3, 3].grid(row=sizz3, column=3)
                    self.cells6[sizz3, 3].insert(0, cells5[inc3][0][2])
                    self.cells6[sizz3, 3].config(state="readonly")

                    self.cells6[sizz3, 4] = Entry(self.scrollable_frame1, width=9)
                    self.cells6[sizz3, 4].grid(row=sizz3, column=4)
                    amount3 = float(self.cells6[sizz3, 2].get())
                    amount4 = float(self.cells6[sizz3, 3].get())
                    total1 = amount3 * amount4
                    self.cells6[sizz3, 4].insert(0, total1)
                    self.cells6[sizz3, 4].config(state="readonly")
                    grnd1 = grnd1 + total1

                  gstlabour = float(grnd1*28/100)
                  gstparts = float(grnd0*28/100)
                  grandttl = float(grnd0+gstparts+grnd1+gstlabour)
                  self.Totalpart.set(grnd0)
                  self.TotalLabour.set(grnd1)
                  self.GstLabour.set(gstlabour)
                  self.GstParts.set(gstparts)
                  self.GrandTotal.set(grandttl)

                  self.KM.set(cells1[fg][2])


                finally:
                  if (connection.is_connected()):
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

              def changeButton(value):
                cell4_len =len(self.cells4)
                cell6_len =len(self.cells6)
                dell4_len =cell4_len -1
                dell6_len =cell6_len -1
                final_cell4 =int(dell4_len/5)
                final_cell6 =int(dell6_len/5)
                final_cell4 = final_cell4 + 1
                final_cell6 = final_cell6 + 1
                if final_cell4 > 1:
                  for row in range(1,final_cell4):
                      self.cells4[row,0].destroy()
                      self.cells4[row,1].destroy()
                      self.cells4[row,2].destroy()
                      self.cells4[row,3].destroy()
                      self.cells4[row,4].destroy()

                if final_cell6 > 1:
                  for row1 in range(1,final_cell6):
                    self.cells6[row1, 0].destroy()
                    self.cells6[row1, 1].destroy()
                    self.cells6[row1, 2].destroy()
                    self.cells6[row1, 3].destroy()
                    self.cells6[row1, 4].destroy()
                viewclick(value)


          else:
            print("Incorrect")

        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




        # Get,Set and connectivity
        # Search Button


      def newjobf(self):
        cell4_len = len(self.cells4)
        cell6_len = len(self.cells6)
        dell4_len = cell4_len - 1
        dell6_len = cell6_len - 1
        final_cell4 = int(dell4_len / 5)
        final_cell6 = int(dell6_len / 5)
        final_cell4 =final_cell4 + 1
        final_cell6 =final_cell6 + 1

        if final_cell4 > 1:
          for row in range (1,final_cell4):
            self.cells4[row, 0].destroy()
            self.cells4[row, 1].destroy()
            self.cells4[row, 2].destroy()
            self.cells4[row, 3].destroy()
            self.cells4[row, 4].destroy()

        if final_cell6 > 1:
          for row1 in range (1,final_cell6):
            self.cells6[row1, 0].destroy()
            self.cells6[row1, 1].destroy()
            self.cells6[row1, 2].destroy()
            self.cells6[row1, 3].destroy()
            self.cells6[row1, 4].destroy()
        self.KM.set("")
        self.vkm_txt.config(state="normal")
        self.TotalLabour.set("")
        self.Totalpart.set("")
        self.GstLabour.set("")
        self.GstParts.set("")
        self.GrandTotal.set("")
        self.entry.config(state="normal")
        self.Reg22_txt.config(state="readonly")
        self.icon_btn.config(state="disabled")
        self.newjob.config(state="disabled")



      def newcustomerf(self):
        self.vclass_txt["values"]=["Scooter","Bike","Hatchback Car","Sedan Car","SUV Car"]
        self.customer.set("")
        self.cname_txt.config(state="normal")
        self.cphone_txt.config(state="normal")
        self.caddress_txt.config(state="normal")
        self.newcustomer.config(state="disabled")
        self.vclass_txt.config(state="readonly")
        self.Reg22_txt.config(state="readonly")
        self.icon_btn.config(state="disabled")
        self.entry.config(state="normal")
        self.vkm_txt.config(state="normal")


      def classvalues(self,event):
        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
          a = self.vclass_txt.get()
          v = []
          if a =="Scooter":
            sql = "SELECT DISTINCT Brand FROM marketed_vehical where Class = %s ;"
            cursor.execute(sql,("Scooter",))
            myresult = cursor.fetchall()
            for i in myresult:
              v.append(i)

          elif a =="Bike":
            sql1 = "SELECT DISTINCT Brand FROM marketed_vehical where Class = %s ;"
            cursor.execute(sql1,("Bike",))
            myresult1 = cursor.fetchall()
            for j in myresult1:
              v.append(j)

          elif a =="Hatchback Car":
            sql2 = "SELECT DISTINCT Brand FROM marketed_vehical where Class = %s ;"
            cursor.execute(sql2,("Hatchback Car",))
            myresult2 = cursor.fetchall()
            for k in myresult2:
              v.append(k)

          elif a =="Sedan Car":
            sql3 = "SELECT DISTINCT Brand FROM marketed_vehical where Class = %s ;"
            cursor.execute(sql3,("Sedan Car",))
            myresult3 = cursor.fetchall()
            for q in myresult3:
              v.append(q)

          elif a =="SUV Car":
            sql4 = "SELECT DISTINCT Brand FROM marketed_vehical where Class = %s ;"
            cursor.execute(sql4,("SUV Car",))
            myresult4 = cursor.fetchall()
            for w in myresult4:
              v.append(w)

          self.vbrand_txt["values"] = v
          self.vbrand_txt.config(state="readonly")

        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

      def brandvalues(self,event):
        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
          a = self.vbrand_txt.get()
          b = self.vclass_txt.get()
          v = []
          sql = "SELECT DISTINCT Model FROM marketed_vehical where Class = %s and Brand = %s ;"
          cursor.execute(sql,(b,a))
          myresult = cursor.fetchall()
          print(myresult)
          for i in myresult:
            v.append(i[0])
          print(v)

          self.vmodel_txt["values"] = v
          self.vmodel_txt.config(state="readonly")
        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


      def modelvalues(self,event):
        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
          a= self.vmodel_txt.get()
          v = []
          sql = "SELECT DISTINCT Year FROM marketed_vehical where Model = %s ;"
          cursor.execute(sql,(a,))
          myresult = cursor.fetchall()
          print(myresult)
          for i in myresult:
            v.append(i[0])
          print(v)
          self.vyear_txt["values"] = v
          self.vyear_txt.config(state="readonly")

        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



      def yearvalues(self,event):
        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
          a = self.vmodel_txt.get()
          b= self.vyear_txt.get()
          v = []
          sql = "SELECT DISTINCT Colour FROM marketed_vehical where Model = %s and Year = %s ;"
          cursor.execute(sql,(a,b))
          myresult = cursor.fetchall()
          print(myresult)
          for i in myresult:
            v.append(i[0])
          print(v)

          self.vcolour_txt["values"] = v
          self.vcolour_txt.config(state="readonly")
        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


      def colourvalues(self,event):
        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
          a= self.vmodel_txt.get()
          b= self.vyear_txt.get()
          v = []
          sql = "SELECT DISTINCT Fuel FROM marketed_vehical where Model = %s and Year = %s ;"
          cursor.execute(sql,(a,b))
          myresult = cursor.fetchall()
          print(myresult)
          for i in myresult:
            v.append(i[0])
          print(v)

          self.vfuel_txt["values"] = v
          self.vfuel_txt.config(state="readonly")
        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

      def fuelvalues(self,event):
        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
          a= self.vmodel_txt.get()
          b= self.vyear_txt.get()
          v = []
          sql = "SELECT DISTINCT Wheels FROM marketed_vehical where Model = %s and Year = %s ;"
          cursor.execute(sql,(a,b))
          myresult = cursor.fetchall()
          print(myresult)
          for i in myresult:
            v.append(i[0])
          print(v)

          self.vwheels_txt["values"] = v
          self.vwheels_txt.config(state="readonly")
        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

      def wheelsvalues(self,event):
        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
          a= self.vmodel_txt.get()
          b= self.vyear_txt.get()
          v = []
          sql = "SELECT DISTINCT CC FROM marketed_vehical where Model = %s and Year = %s ;"
          cursor.execute(sql,(a,b))
          myresult = cursor.fetchall()
          print(myresult)
          for i in myresult:
            v.append(i[0])
          print(v)

          self.vcc_txt["values"] = v
          self.vcc_txt.config(state="readonly")
        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

      def ccvalues(self,event):
        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
          a= self.vmodel_txt.get()
          b= self.vyear_txt.get()
          v = []
          sql = "SELECT DISTINCT Gear FROM marketed_vehical where Model = %s and Year = %s ;"
          cursor.execute(sql,(a,b))
          myresult = cursor.fetchall()
          print(myresult)
          for i in myresult:
            v.append(i[0])
          print(v)

          self.vgear_txt["values"] = v
          self.vgear_txt.config(state="readonly")
        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

      def gearvalues(self,event):
        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
          a= self.vmodel_txt.get()
          b= self.vyear_txt.get()
          v = []
          sql = "SELECT DISTINCT Power_HP FROM marketed_vehical where Model = %s and Year = %s ;"
          cursor.execute(sql,(a,b))
          myresult = cursor.fetchall()
          print(myresult)
          for i in myresult:
            v.append(i[0])
          print(v)

          self.vpower_txt["values"] = v
          self.vpower_txt.config(state="readonly")
        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



      #Job Card Functions and Events for Create Job And Create Customer
      def listbox_show(self, j):
       if self.entry["state"] == NORMAL:
          self.entry.delete(0,END)
          try:
             connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
             if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

             table_check = self.vclass_txt.get()
             if table_check == "Scooter":
               table_name = 'scooter_parts'

             elif table_check == "Bike":
               table_name = 'bike_parts'

             elif table_check == "Hatchback Car":
               table_name = 'hatchback_car_parts'

             elif table_check == "Sedan Car":
               table_name = 'sedan_car_parts'

             elif table_check == "SUV Car":
               table_name = 'suv_car_parts'

             # parts table
             sql1 = "SELECT * FROM {} where Model = %s ;".format(table_name)
             vehsql = self.vmodel_txt.get()
             cursor.execute(sql1, (vehsql,))
             myresult1 = cursor.fetchall()
             inss = 0
             for y in myresult1:
                self.cells7[inss] = (y)
                inss += 1
             print(self.cells7)
             # job performed
             sql2 = "SELECT * FROM job_performed ;"
             cursor.execute(sql2, )
             myresult2 = cursor.fetchall()
             print(myresult2)
             inss1 = 0
             for zz in myresult2:
                self.cells8[inss1] = (zz)
                inss1 += 1
             print(self.cells8)
             self.test_list = []
             lencell7 = len(self.cells7)
             print(lencell7)
             for x in range(lencell7):
                self.test_list.append(self.cells7[x][3])

             lencell8 = len(self.cells8)
             print(lencell8)
             for tt in range(lencell8):
                self.test_list.append(self.cells8[tt][1])

             print(self.test_list)
             self.listbox.destroy()
             self.listbox = Listbox(self.FF32,width=27)
             self.listbox.place(x=446, y=36)
             # listbox.bind('<Double-Button-1>', on_select)
             self.listbox.bind('<<ListboxSelect>>', self.on_select)
             self.listbox_update(self.test_list)

          finally:
             if (connection.is_connected()):
                 cursor.close()
                 connection.close()
                 print("MySQL connection is closed")

      def on_keyrelease(self, event):

        # get text from entry
        value = event.widget.get()
        value = value.strip().lower()

        # get data from test_list
        if value == '' or value.isspace() == TRUE:
          data = self.test_list
        else:
          data = []
          for item in self.test_list:
            if value in item.lower():
              data.append(item)

        # update data in listbox
        self.listbox_update(data)

      def listbox_update(self, data):
        # delete previous data
        self.listbox.delete(0, 'end')

        # sorting data
        data = sorted(data, key=str.lower)
        # put new data
        for item in data:
          self.listbox.insert('end', item)

      def on_select(self, event):
        # display element selected on list
        print('(event) previous:', event.widget.get('active'))
        print('(event)  current:', event.widget.get(event.widget.curselection()))
        value1 = event.widget.get(event.widget.curselection())
        print(value1)
        lencell9 = len(self.cells9)
        mincell9 = lencell9 - 1
        totlcell9 = int(mincell9 / 5 + 1)
        print(totlcell9)
        checkval = 0
        for i in self.cells7:
          if value1 == self.cells7[checkval][3]:
            self.cells9[totlcell9, 0] = Entry(self.scrollable_frame2, width=7)
            self.cells9[totlcell9, 0].grid(row=totlcell9, column=0)
            self.cells9[totlcell9, 0].insert(0, self.cells7[checkval][1])
            self.cells9[totlcell9, 0].config(state="readonly")

            self.cells9[totlcell9, 1] = Entry(self.scrollable_frame2, width=62)
            self.cells9[totlcell9, 1].grid(row=totlcell9, column=1)
            self.cells9[totlcell9, 1].insert(0, self.cells7[checkval][3])
            self.cells9[totlcell9, 1].config(state="readonly")

            self.cells9[totlcell9, 2] = Entry(self.scrollable_frame2, width=9)
            self.cells9[totlcell9, 2].grid(row=totlcell9, column=2)
            # self.cells9[totlcell9,2].bind('<KeyRelease>',self.autocalculation)
            self.cells9[totlcell9, 2].bind("<KeyRelease>",
                                           lambda event, cellno=9, rowno=totlcell9: self.autocalculation(event, cellno,
                                                                                                         rowno))

            self.cells9[totlcell9, 3] = Entry(self.scrollable_frame2, width=9)
            self.cells9[totlcell9, 3].grid(row=totlcell9, column=3)
            self.cells9[totlcell9, 3].insert(0, self.cells7[checkval][4])
            self.cells9[totlcell9, 3].config(state="readonly")

            self.cells9[totlcell9, 4] = Entry(self.scrollable_frame2, width=9)
            self.cells9[totlcell9, 4].grid(row=totlcell9, column=4)
            self.cells9[totlcell9, 4].config(state="readonly")
          checkval = checkval + 1

        lencell10 = len(self.cells10)
        mincell10 = lencell10 - 1
        totlcell10 = int(mincell10 / 5 + 1)
        print(totlcell10)
        checkval2 = 0


        for i in self.cells8:
          if value1 == self.cells8[checkval2][1]:
            self.cells10[totlcell10, 0] = Entry(self.scrollable_frame1, width=7)
            self.cells10[totlcell10, 0].grid(row=totlcell10, column=0)
            self.cells10[totlcell10, 0].insert(0, self.cells8[checkval2][0])
            self.cells10[totlcell10, 0].config(state="readonly")

            self.cells10[totlcell10, 1] = Entry(self.scrollable_frame1, width=62)
            self.cells10[totlcell10, 1].grid(row=totlcell10, column=1)
            self.cells10[totlcell10, 1].insert(0, self.cells8[checkval2][1])
            self.cells10[totlcell10, 1].config(state="readonly")

            self.cells10[totlcell10, 2] = Entry(self.scrollable_frame1, width=9)
            self.cells10[totlcell10, 2].grid(row=totlcell10, column=2)
            # self.cells10[totlcell10,2].bind('<KeyRelease>',self.autocalculation)
            self.cells10[totlcell10, 2].bind("<KeyRelease>",lambda event, cellno=10, rowno=totlcell10: self.autocalculation(event,cellno,rowno))

            self.cells10[totlcell10, 3] = Entry(self.scrollable_frame1, width=9)
            self.cells10[totlcell10, 3].grid(row=totlcell10, column=3)
            self.cells10[totlcell10, 3].insert(0, self.cells8[checkval2][2])
            self.cells10[totlcell10, 3].config(state="readonly")

            self.cells10[totlcell10, 4] = Entry(self.scrollable_frame1, width=9)
            self.cells10[totlcell10, 4].grid(row=totlcell10, column=4)
            self.cells10[totlcell10, 4].config(state="readonly")
          checkval2 = checkval2 + 1

        print('---')
        self.entry.delete(0,END)
        self.entry.insert(0,"Search")
        self.listbox.destroy()

      def autocalculation(self, event, cellno, rowno):
        value0 = event.widget.get()
        if value0.isspace() == TRUE or value0 == '':
          if cellno == 9:
            self.cells9[rowno, 4].config(state="normal")
            self.cells9[rowno, 4].delete(0, END)
            self.cells9[rowno, 4].config(state="readonly")
          elif cellno == 10:
            self.cells10[rowno, 4].config(state="normal")
            self.cells10[rowno, 4].delete(0, END)
            self.cells10[rowno, 4].config(state="readonly")

        else:
          value2 = float(value0)
          print(value2)
          print(cellno)
          print(rowno)
          find = re.compile(r"^\d*[.,]?\d*$")

          if find.match(value0):
            print('TRUE')
            if cellno == 9:
              rate0 = self.cells9[rowno, 3].get()
              rate1 = float(rate0)
              print(rate1)
              self.cells9[rowno, 4].config(state="normal")
              self.cells9[rowno, 4].delete(0, END)
              self.cells9[rowno, 4].insert(0, value2 * rate1)
              self.cells9[rowno, 4].config(state="readonly")

              lenthofcell =len(self.cells9)
              lenthminus =lenthofcell-1
              finallenth =int(lenthminus/5+1)
              Sum=0.0
              for i in range(1,finallenth):
                amount = self.cells9[i,4].get()
                if amount.isspace() == TRUE or amount == '':
                    pass
                else:
                    amount1 =float(amount)
                    Sum =Sum+amount1

                self.Totalpart.set(str(Sum))
                gst=(Sum*28/100)
                self.GstParts.set(str(gst))
                labour =self.TotalLabour.get()
                if labour =='':
                  labour1=0.0
                else:
                   labour1 =float(labour)
                gstlabour=self.GstLabour.get()
                if gstlabour =='':
                  gstlabour1=0.0
                else:
                  gstlabour1=float(gstlabour)
                finalamount=Sum+gst+labour1+gstlabour1
                self.GrandTotal.set(str(finalamount))


            if cellno == 10:
              rate2 = self.cells10[rowno, 3].get()
              rate3 = float(rate2)
              self.cells10[rowno, 4].config(state="normal")
              self.cells10[rowno, 4].delete(0, END)
              self.cells10[rowno, 4].insert(0, value2 * rate3)
              self.cells10[rowno, 4].config(state="readonly")

              lenthofcell1 = len(self.cells10)
              lenthminus1 = lenthofcell1 - 1
              finallenth1 = int(lenthminus1 / 5 + 1)
              Sum1 = 0.0
              for j in range(1,finallenth1):
                amount2 = self.cells10[j, 4].get()
                if amount2.isspace() == TRUE or amount2 == '':
                  pass
                else:
                  amount3 = float(amount2)
                  Sum1 = Sum1 + amount3

                self.TotalLabour.set(str(Sum1))
                gst1 = (Sum1 * 28 / 100)
                self.GstLabour.set(str(gst1))
                parts2 = self.Totalpart.get()
                if parts2 =='':
                  parts3 = 0.0
                else:
                  parts3 = float(parts2)
                gstparts2 = self.GstParts.get()
                if gstparts2 =='':
                  gstparts3 =0.0
                else:
                  gstparts3 = float(gstparts2)
                finalamount1 = Sum1 + gst1 + parts3 + gstparts3
                self.GrandTotal.set(str(finalamount1))

          else:
            print("False")



      def savebutton(self):
        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

          a = str(self.vclass_txt.get())
          b = str(self.vbrand_txt.get())
          c = str(self.vmodel_txt.get())
          d = str(self.vyear_txt.get())
          e = str(self.vcolour_txt.get())
          f = str(self.vfuel_txt.get())
          g = str(self.vwheels_txt.get())
          h = str(self.vcc_txt.get())
          i = str(self.vgear_txt.get())
          j = str(self.vpower_txt.get())

          cus_name = str(self.cname_txt.get())
          cus_phone = str(self.cphone_txt.get())
          cus_address = str(self.caddress_txt.get("1.0", END))
          latest_KM1 = self.vkm_txt.get()
          print(latest_KM1)
          latest_KM = str(latest_KM1)
          reg11=re.compile('^[0-9]*$')
          if a == "Select" or b== "Select" or c=="Select" or d=="Select" or e=="Select" or f=="Select" or g=="Select" or h=="Select" or i=="Select" or j=="Select" :
            messagebox.showerror("Incomplete","Please Select Or fill all the necessary details Correctly.")
          elif len(cus_address) >144 :
            messagebox.showerror(("Not Valid Address","Please only enter less than 144 Characters including Spaces"))
          elif len(cus_phone) >10 or len(cus_phone) < 10:
            messagebox.showerror("Not Valid Phone Number","Please Enter A Valid 10 digit Number")

          else:
                 sql = "SELECT S_No from marketed_vehical where Class = %s and Brand = %s and Model = %s and Year = %s and Colour = %s and Fuel = %s and Wheels = %s and CC = %s and Gear = %s and Power_HP = %s ;"
                 cursor.execute(sql, (a, b, c, d, e, f, g, h, i, j))
                 myresult = cursor.fetchall()
                 vehical_Sno = myresult[0][0]
                 print(vehical_Sno)


                 sql1 = "SELECT max(S_NO) from customer_details ;"
                 cursor.execute(sql1, )
                 myresult1 = cursor.fetchall()
                 customer_Sno1 = (myresult1[0][0]) + 1
                 print(customer_Sno1)
                 customer_Sno=str(customer_Sno1)

                 sql2 = "SELECT max(S_NO) from job_card ;"
                 cursor.execute(sql2, )
                 myresult2 = cursor.fetchall()
                 jobcard_Sno1 = (myresult2[0][0]) + 1
                 print(jobcard_Sno1)
                 jobcard_Sno =str(jobcard_Sno1)

                 table_check = self.vclass_txt.get()
                 if table_check == "Scooter":
                      table_name = 'scooter_parts'

                 elif table_check == "Bike":
                      table_name = 'bike_parts'

                 elif table_check == "Hatchback Car":
                      table_name = 'hatchback_car_parts'

                 elif table_check == "Sedan Car":
                      table_name = 'sedan_car_parts'

                 elif table_check == "SUV Car":
                      table_name = 'suv_car_parts'

                 jobperformed_S_no = ""
                 jobhours_nos = ""
                 cell10len = len(self.cells10)
                 if cell10len > 1:
                   minuscell10 = cell10len - 1
                   finalcell10 = int(minuscell10 / 5 + 1)
                   for j in range(1, finalcell10):
                     jobname = self.cells10[j, 1].get()
                     sql4 = "SELECT S_NO from job_performed where Job_Name = %s ;"
                     cursor.execute(sql4, (jobname,))
                     myresult4 = cursor.fetchall()
                     jobname_Sno = myresult4[0][0]
                     jobperformed_S_no = jobperformed_S_no + str(jobname_Sno) + ","

                     jobhours1 = self.cells10[j, 2].get()
                     jobhours_nos = jobhours_nos + str(jobhours1) + ","

                   print(jobperformed_S_no)
                   print(jobhours_nos)

                   if cell10len > 1:
                    if jobhours_nos.find(",,") ==-1:
                      if jobhours_nos[0] ==",":
                         messagebox.showerror("Empty Field in Job Card","Please Fill the No of Hours")
                      else:
                        print("not found")
                    else:
                      messagebox.showerror("Empty Field in Job Card", "Please Fill the No of Hours")
                 parts_S_no1 = ""
                 quantity_nos = ""
                 cell9len = len(self.cells9)
                 if cell9len > 1:
                      minuscell9 = cell9len - 1
                      finalcell9 = int(minuscell9 / 5 + 1)
                      for i in range(1, finalcell9):
                          partname = self.cells9[i, 1].get()
                          sql3 = "SELECT S_NO from {} where Part_Name = %s ;".format(table_name)
                          cursor.execute(sql3, (partname,))
                          myresult3 = cursor.fetchall()
                          partname_Sno = myresult3[0][0]
                          parts_S_no1 = parts_S_no1 + str(partname_Sno) + ","

                          quantity1 = self.cells9[i, 2].get()
                          quantity_nos = quantity_nos + str(quantity1) + ","
                          print(parts_S_no1)
                          print(quantity_nos)
                          if quantity_nos.find(",,") ==-1:
                             if quantity_nos[0] == ",":
                               if cell9len > 1:
                                  messagebox.showerror("Empty Field in Job Card","Please Fill the No of Quantity")
                             else:
                               print("not found2")
                          else:
                            messagebox.showerror("Empty Field in Job Card","Please Fill the No of Quantity")

                 import random
                 import math

                 data = "0123456789"
                 leng = len(data)

                 invoice_no = ""

                 for i in range(5):
                      invoice_no += data[math.floor(random.random() * leng)]

                 print(invoice_no)
                 self.invoice_no1 = str(invoice_no)

                 sql0 = "SELECT Registration_No from customer_details where Registration_No = %s ;"
                 research = self.regsearch.get()
                 cursor.execute(sql0, (research,))
                 myresult0 = cursor.fetchall()
                 print(myresult0)
                 if len(myresult0) == 0:
                    finalresult0 = '0'
                 else:
                    finalresult0 = myresult0[0][0]

                 if finalresult0 != research:
                    if messagebox.askyesno("Are You Sure","The Details you entered Once Saved won't be changed. IF Correct then Click on 'Yes' otherwise 'No'")== TRUE:
                        sql5 = "INSERT INTO customer_details VALUES( %s, %s ,%s , %s , %s , %s );"
                        cursor.execute(sql5,(customer_Sno, research, cus_name, cus_phone, cus_address, vehical_Sno))
                        connection.commit()
                        print(cursor.rowcount, "record5 inserted.")

                        sql6 = "INSERT INTO job_card VALUES(%s , %s , %s , %s, %s , %s , %s ,curdate(),curtime(), %s) ;"
                        cursor.execute(sql6, (jobcard_Sno, research, latest_KM, parts_S_no1, jobhours_nos, quantity_nos,self.invoice_no1, jobperformed_S_no))
                        connection.commit()
                        print(cursor.rowcount, "record6 inserted.")
                        self.Generate_btn.config(state="normal")

                 else:
                    sql7 = "INSERT INTO job_card VALUES(%s , %s , %s , %s, %s , %s , %s ,curdate(),curtime(), %s) ;"
                    cursor.execute(sql7, (jobcard_Sno, research, latest_KM, parts_S_no1, jobhours_nos, quantity_nos, self.invoice_no1,jobperformed_S_no))
                    connection.commit()
                    print(cursor.rowcount, "record6 inserted.")
                    self.Generate_btn.config(state="normal")






        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



      def generatebill(self):
        import webbrowser
        from reportlab.pdfgen import canvas
        from reportlab.platypus import Paragraph, Table, TableStyle, Frame
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.units import inch
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.lib.enums import TA_CENTER
        from reportlab.pdfbase.ttfonts import TTFont, TTEncoding
        pdf = canvas.Canvas("pdf2342.pdf", pagesize=A4)
        flow_obj = []
        styles = getSampleStyleSheet()

        # Company Name
        p = ParagraphStyle('test')
        p.textColor = 'black'
        p.borderColor = 'black'
        p.alignment = TA_CENTER
        p.fontSize = 15
        text1 = Paragraph("Shiva Auto Services", p)
        flow_obj.append(text1)
        frame1 = Frame(5, 800, 150, 40, showBoundary=0)
        frame1.addFromList(flow_obj, pdf)

        # Tagline
        p1 = ParagraphStyle('test')
        p1.textColor = 'black'
        p1.borderColor = 'black'
        p1.alignment = TA_CENTER
        p1.fontSize = 8
        text1 = Paragraph("The Art of Performance", p1)
        flow_obj.append(text1)
        frame1 = Frame(5, 785, 130, 35, showBoundary=0)
        frame1.addFromList(flow_obj, pdf)

        # invoice
        p2 = ParagraphStyle('test')
        p2.textColor = 'black'
        p2.borderColor = 'black'
        p2.alignment = TA_CENTER
        p2.fontSize = 25
        text1 = Paragraph("INVOICE", p2)
        flow_obj.append(text1)
        frame1 = Frame(430, 800, 200, 40, showBoundary=0)
        frame1.addFromList(flow_obj, pdf)

        try:
          connection = mysql.connector.connect(host='localhost', database='bill', user='root', password='login')
          if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

          sql = "SELECT Bill_Date from job_card where Invoice_NO = %s ;"
          cursor.execute(sql, (self.invoice_no1,))
          myresult = cursor.fetchall()
          datefromdb =str(myresult[0][0])


        finally:
          if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



        # Date and Invoice No.
        column_width1 = 2.06 * inch
        column_width2 = 3.0 * inch
        column_width3 = 2.06 * inch
        column_width4 = 2.06 * inch
        t = Table([["DATE", datefromdb, "INVOICE #", "INV-00-"+self.invoice_no1]], colWidths=[2.06 * inch] * 5)
        ts = TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.white),
                         ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                         ("TEXTCOLOR", (0, 0), (0, 0), colors.blue),
                         ("TEXTCOLOR", (2, 0), (2, 0), colors.blue),
                         ("ALIGN", (2, 0), (2, 0), 'RIGHT')

                         ])
        t.setStyle(ts)
        flow_obj.append(t)
        frame1 = Frame(0, 758, 595, 30, showBoundary=0)
        frame1.addFromList(flow_obj, pdf)

        # Customer info and vehical info header
        column_width9 = 2.06 * inch
        column_width10 = 3.0 * inch
        column_width11 = 2.06 * inch
        column_width12 = 2.06 * inch
        t = Table([["CUSTOMER INFO", "", "VEHICLE INFO", ""]], colWidths=[2.06 * inch] * 5)
        ts = TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.blue),
                         ("TEXTCOLOR", (0, 0), (-1, 0), colors.white)
                         ])
        t.setStyle(ts)
        flow_obj.append(t)
        frame1 = Frame(0, 730, 595, 30, showBoundary=0)
        frame1.addFromList(flow_obj, pdf)

        # Customer info and vehical info

        address1 =str(self.caddress_txt.get(1.0,END))
        print(type(address1))
        length1 = len(address1)
        length2 =length1-1
        print(length1)
        line1 = ""
        line2 = ""
        line3 = ""
        if length1 > 96 and length1 <= 144:
          line1 = address1[0:48] + "-"
          line2 = address1[49:96] + "-"
          line3 = address1[97:length2]
        elif length1 > 48 and length1 <= 96:
          line1 = address1[0:48] + "-"
          line2 = address1[49:length2]
        else:
          line1 = address1[0:length2]
        print(line1)

        column_width5 = 2.06 * inch
        column_width6 = 3.0 * inch
        column_width7 = 2.06 * inch
        column_width8 = 2.06 * inch
        t = Table([["NAME:", self.customer.get(), "BRAND",self.Brand.get() ],
                   ["", "", "MODEL",self.model.get()],
                   ["ADDRESS:",line1, "YEAR", self.year.get()],
                   ["",line2, "COLOR", self.colour.get()],
                   ["",line3, "CC", self.cc.get()],
                   ["Phone No:",self.Phone.get(), "REG#",self.regsearch.get()],
                   ["", "", "KM", self.KM.get()]], colWidths=[2.06 * inch] * 5)
        ts = TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.lightblue),
                          #("GRID",(0,0),(-1,-1),1,colors.yellow),
                         ("TEXTCOLOR", (0, 0), (-1, -1), colors.blue),
                         ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
                         ("ALIGN", (1, 0), (1, 6), "LEFT"),
                         ("ALIGN", (3, 0), (3, 6), "LEFT"),
                         ("TEXTCOLOR", (1, 0), (1, 6), colors.black),
                         ("TEXTCOLOR", (3, 0), (3, 6), colors.black),

                         ])
        t.setStyle(ts)
        flow_obj.append(t)
        frame1 = Frame(0, 592, 595, 150, showBoundary=0)
        frame1.addFromList(flow_obj, pdf)

        # Job Performed

        jobperformed_data =[["Job Performed", "Hours", "Rate", "Amount"],
                   ["", "", "", "-"],
                   ["", "", "", "-"],
                   ["", "", "", "-"],
                   ["", "", "", "-"],
                   ["", "", "", "-"],
                   ["", "", "", "-"],
                   ["", "", "", "-"],
                   ["", "", "", "-"], ]
        lencell10 = len(self.cells10)
        minuscell10 =lencell10-1
        finalcell10 =int(minuscell10/5 +1)

        if finalcell10>1:
          for i in range(1,finalcell10):
            jobperformed_data[i][0] = str(self.cells10[i,1].get())
            jobperformed_data[i][1] = str(self.cells10[i,2].get())
            jobperformed_data[i][2] = str(self.cells10[i,3].get())
            jobperformed_data[i][3] = str(self.cells10[i,4].get())


        column_width13 = 5.09 * inch
        column_width14 = 1.06 * inch
        column_width15 = 1.06 * inch
        column_width16 = 1.06 * inch
        t = Table(jobperformed_data, colWidths=[column_width13, column_width14, column_width15, column_width16] * 5)
        ts = TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.blue),
                         ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                         ("GRID", (0, 1), (-1, -1), 1, colors.black),
                         ("ALIGN", (1, 0), (1, 8), "CENTER"),
                         ("ALIGN", (2, 0), (2, 8), "CENTER"),
                         ("ALIGN", (3, 0), (3, 8), "CENTER"),

                         ])
        t.setStyle(ts)
        flow_obj.append(t)
        frame1 = Frame(0, 436, 595, 180, showBoundary=0)
        frame1.addFromList(flow_obj, pdf)

        # Job Performed Calculation
        column_width17 = 5.68 * inch
        column_width18 = 1.0 * inch
        column_width19 = 0.5 * inch
        column_width20 = 1.06 * inch
        rupee_uni = "\u20B9"
        print(rupee_uni)
        t = Table([["", "SUBTOTAL", "$", self.TotalLabour.get()],
                   ["", "GST", "28%", self.GstLabour.get()]],
                  colWidths=[column_width17, column_width18, column_width19, column_width20] * 5)
        ts = TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.white),
                         ("TEXTCOLOR", (0, 0), (-1, -1), colors.blue),
                         # ("GRID",(0,0),(-1,-1),1,colors.black),
                         ("ALIGN", (0, 0), (-1, -1), "CENTER")
                         ])
        t.setStyle(ts)
        flow_obj.append(t)
        frame1 = Frame(0, 400, 595, 50, showBoundary=0)
        frame1.addFromList(flow_obj, pdf)

        # Parts

        Partspurchaced_data = [["PART #", "PART NAME", "QTY", "UNIT PRICE", "AMOUNT"],
                   ["", "", "", "", "-"],
                   ["", "", "", "", "-"],
                   ["", "", "", "", "-"],
                   ["", "", "", "", "-"],
                   ["", "", "", "", "-"],
                   ["", "", "", "", "-"],
                   ["", "", "", "", "-"],
                   ["", "", "", "", "-"], ]

        lencell9 = len(self.cells9)
        minuscell9 = lencell9 - 1
        finalcell9 = int(minuscell9 / 5 + 1)

        if finalcell9 > 1:
          for j in range(1, finalcell9):
            Partspurchaced_data[j][0] = str(self.cells9[j, 0].get())
            Partspurchaced_data[j][1] = str(self.cells9[j, 1].get())
            Partspurchaced_data[j][2] = str(self.cells9[j, 2].get())
            Partspurchaced_data[j][3] = str(self.cells9[j, 3].get())
            Partspurchaced_data[j][4] = str(self.cells9[j, 4].get())


        column_width21 = 0.7 * inch
        column_width22 = 4.5 * inch
        column_width23 = 1.00 * inch
        column_width24 = 1.00 * inch
        column_width25 = 1.06 * inch
        t = Table(Partspurchaced_data,colWidths=[column_width21, column_width22, column_width23, column_width24, column_width25] * 5)
        ts = TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.blue),
                         ("GRID", (0, 0), (-1, -1), 1, colors.black),
                         ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                         ("ALIGN", (2, 0), (2, 8), "CENTER"),
                         ("ALIGN", (3, 0), (3, 8), "CENTER"),
                         ("ALIGN", (4, 0), (4, 8), "CENTER"),
                         ])
        t.setStyle(ts)
        flow_obj.append(t)
        frame1 = Frame(0, 230, 595, 180, showBoundary=0)
        frame1.addFromList(flow_obj, pdf)

        # Parts Calculation

        labourgst =float(self.GstLabour.get())
        partsgst  =float(self.GstParts.get())
        Total_Gst =labourgst+partsgst

        column_width26 = 1.06 * inch
        column_width27 = 0.5 * inch
        column_width28 = 1.06 * inch
        t = Table([["SUBTOTAL", "$", self.Totalpart.get()],
                   ["GST", "28%", self.GstParts.get()],
                   ["", "", ""],
                   ["TOTAL LABOUR", "$",self.TotalLabour.get()],
                   ["TOTAL PARTS", "$", self.Totalpart.get()],
                   ["GST", "$", Total_Gst],
                   ["TOTAL", "$", self.GrandTotal.get()]], colWidths=[column_width26, column_width27, column_width28] * 5)
        ts = TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.white),
                         ("TEXTCOLOR", (0, 0), (-1, -1), colors.blue),
                         # ("GRID",(0,0),(-1,-1),1,colors.black),
                         ("ALIGN", (0, 0), (-1, -1), "CENTER")
                         ])
        t.setStyle(ts)
        flow_obj.append(t)
        frame1 = Frame(400, 94, 210, 150, showBoundary=0)
        frame1.addFromList(flow_obj, pdf)

        # COMMENTS FRAME
        p3 = ParagraphStyle('test')
        p3.textColor = 'blue'
        p3.borderColor = 'black'
        p3.alignment = TA_CENTER
        p3.fontSize = 10
        text1 = Paragraph("COMMENTS", p3)
        flow_obj.append(text1)
        frame = Frame(-10, 185, 100, 30, showBoundary=0)
        frame.addFromList(flow_obj, pdf)

        # Comment Text Frame
        p4 = ParagraphStyle('test')
        p4.textColor = 'black'
        p4.borderColor = 'black'
        p4.alignment = TA_CENTER
        p4.fontSize = 8
        text1 = Paragraph("Please include the invoice number as reference when paying online or by check", p4)
        flow_obj.append(text1)
        frame = Frame(-8, 166, 320, 30, showBoundary=0)
        frame.addFromList(flow_obj, pdf)

        # Make all Line
        p5 = ParagraphStyle('test')
        p5.textColor = 'black'
        p5.borderColor = 'black'
        p5.alignment = TA_CENTER
        p5.fontSize = 8
        text1 = Paragraph("Make all checks payable to", p5)
        flow_obj.append(text1)
        frame = Frame(373, 80, 150, 30, showBoundary=0)
        frame.addFromList(flow_obj, pdf)

        # Shiva Auto Services
        p6 = ParagraphStyle('test')
        p6.textColor = 'blue'
        p6.borderColor = 'black'
        p6.alignment = TA_CENTER
        p6.fontSize = 10
        text1 = Paragraph("Shiva Auto Services", p6)
        flow_obj.append(text1)
        frame = Frame(380, 72, 130, 30, showBoundary=0)
        frame.addFromList(flow_obj, pdf)

        # Thankq For the Business
        p7 = ParagraphStyle('test')
        p7.textColor = 'blue'
        p7.borderColor = 'black'
        p7.alignment = TA_CENTER
        p7.fontSize = 12
        text1 = Paragraph("Thank you for your business!", p6)
        flow_obj.append(text1)
        frame = Frame(0, 80, 150, 30, showBoundary=0)
        frame.addFromList(flow_obj, pdf)

        # Enquiry Details
        p8 = ParagraphStyle('test')
        p8.textColor = 'black'
        p8.borderColor = 'black'
        p8.alignment = TA_CENTER
        p8.fontSize = 8
        text1 = Paragraph(
          "Should you have any enquiries concerning this invoice, please contact Mr. Shiva on 9562458585", p8)
        flow_obj.append(text1)
        frame = Frame(0, 25, 595, 30, showBoundary=0)
        frame.addFromList(flow_obj, pdf)

        # Final Contect Information
        t = Table([["127, Juhu Street, Indira Nagar, Housing Colony, Mandsaur, M.P, India, 458001"],
                   [
                     "Tel: +91 9654895656 Fax: 2-555-898-2635 Email: info@shivaautoservices.com Web: www.shivaautoservices.com "]],
                  colWidths=[8.23 * inch])
        ts = TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.blue),
                         ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
                         # ("GRID",(0,0),(-1,-1),1,colors.black),
                         ('FONTSIZE', (0, 0), (-1, -1), 8),
                         ("ALIGN", (0, 0), (-1, -1), "CENTER")
                         ])
        t.setStyle(ts)
        flow_obj.append(t)
        frame = Frame(0, -15, 596, 57, showBoundary=0)
        frame.addFromList(flow_obj, pdf)

        # First line
        pdf.setLineWidth(6)
        pdf.setStrokeColorRGB(0.1, 0.32, 0.3)
        pdf.line(0, 785, 600, 785)

        # Second Line
        pdf.setLineWidth(6)
        pdf.setStrokeColorRGB(0.1, 0.32, 0.3)
        pdf.line(0, 446, 600, 446)

        # Third Line
        pdf.setLineWidth(6)
        pdf.setStrokeColorRGB(0.1, 0.32, 0.3)
        pdf.line(0, 240, 600, 240)

        # Fourth Line
        pdf.setLineWidth(2)
        pdf.setStrokeColor(colors.black)
        pdf.line(400, 128, 600, 128)

        # Fifth Line
        pdf.setLineWidth(2)
        pdf.setStrokeColor(colors.black)
        pdf.line(0, 195, 400, 195)

        pdf.save()

        webbrowser.open_new("pdf2342.pdf")
        self.Generate_btn.config(state="normal")

      def clearall(self):
        cell4_len = len(self.cells4)
        cell6_len = len(self.cells6)
        dell4_len = cell4_len - 1
        dell6_len = cell6_len - 1
        final_cell4 = int(dell4_len / 5)
        final_cell6 = int(dell6_len / 5)
        final_cell4 = final_cell4 + 1
        final_cell6 = final_cell6 + 1

        if final_cell4 > 1:
          for row in range(1, final_cell4):
            self.cells4[row, 0].destroy()
            self.cells4[row, 1].destroy()
            self.cells4[row, 2].destroy()
            self.cells4[row, 3].destroy()
            self.cells4[row, 4].destroy()

        if final_cell6 > 1:
          for row1 in range(1, final_cell6):
            self.cells6[row1, 0].destroy()
            self.cells6[row1, 1].destroy()
            self.cells6[row1, 2].destroy()
            self.cells6[row1, 3].destroy()
            self.cells6[row1, 4].destroy()

        self.cells4.clear()
        self.cells4[0,0] =Entry()
        self.cells6.clear()
        self.cells6[0,0] =Entry()

        cell2_len = len(self.cells2)
        dell2_len = cell2_len - 1
        final_cell2 = int(dell2_len / 5 +1)
        if final_cell2 > 1:
          for row3 in range(1, final_cell2):
            self.cells2[row3, 0].destroy()
            self.cells2[row3, 1].destroy()
            self.cells2[row3, 2].destroy()
            self.cells2[row3, 3].destroy()
            self.cells2[row3, 4].destroy()

        self.cells2.clear()
        self.cells2[0,0] =Entry()

        self.cells7.clear()
        self.cells8.clear()

        cell9_len = len(self.cells9)
        dell9_len = cell9_len - 1
        final_cell9 = int(dell9_len / 5 + 1)
        if final_cell9 > 1:
          for row4 in range(1, final_cell9):
            self.cells9[row4, 0].destroy()
            self.cells9[row4, 1].destroy()
            self.cells9[row4, 2].destroy()
            self.cells9[row4, 3].destroy()
            self.cells9[row4, 4].destroy()

        cell10_len = len(self.cells10)
        dell10_len = cell10_len - 1
        final_cell10 = int(dell10_len / 5 + 1)
        if final_cell10 > 1:
          for row5 in range(1, final_cell2):
            self.cells10[row5, 0].destroy()
            self.cells10[row5, 1].destroy()
            self.cells10[row5, 2].destroy()
            self.cells10[row5, 3].destroy()
            self.cells10[row5, 4].destroy()

        self.cells9.clear()
        self.cells9[0,0] =Entry()
        self.cells10.clear()
        self.cells10[0,0] =Entry()

        self.KM.set("")
        self.vkm_txt.config(state="readonly")
        self.entry.config(state="readonly")
        self.regsearch.set("")
        self.Reg22_txt.config(state="normal")
        self.icon_btn.config(state="normal")
        self.Generate_btn.config(state="disabled")
        self.customer.set("")
        self.Phone.set("")
        self.caddress_txt.config(state="normal")
        self.caddress_txt.delete(1.0,END)
        self.caddress_txt.config(state="disabled")
        self.cname_txt.config(state="readonly")
        self.cphone_txt.config(state="readonly")
        self.vclass_txt.set("")
        self.vclass_txt.config(state="disabled")
        self.vbrand_txt.set("")
        self.vbrand_txt.config(state="disabled")
        self.vmodel_txt.set("")
        self.vmodel_txt.config(state="disabled")
        self.vyear_txt.set("")
        self.vyear_txt.config(state="disabled")
        self.vcolour_txt.set("")
        self.vcolour_txt.config(state="disabled")
        self.vfuel_txt.set("")
        self.vfuel_txt.config(state="disabled")
        self.vwheels_txt.set("")
        self.vwheels_txt.config(state="disabled")
        self.vcc_txt.set("")
        self.vcc_txt.config(state="disabled")
        self.vgear_txt.set("")
        self.vgear_txt.config(state="disabled")
        self.vpower_txt.set("")
        self.vpower_txt.config(state="disabled")
        self.TotalLabour.set("")
        self.Totalpart.set("")
        self.GrandTotal.set("")
        self.GstLabour.set("")
        self.GstParts.set("")
        self.newjob.config(state="disabled")
        self.newcustomer.config(state="disabled")

      def exitbutton(self):
        sys.exit(0)