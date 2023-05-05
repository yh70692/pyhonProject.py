# -*- coding: utf-8 -*-
"""
Created on Wed May 25 09:34:32 2022

@author: Yassin 
"""
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 
import tkinter.messagebox as tkMessageBox


class faultLog:
    def __init__(self, window):

       #====================Variables==========================
        self.full_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.contact_number = tk.IntVar()
        self.apartment_name = tk.StringVar()
        self.date_of_reporting = tk.StringVar()
        self.unit_number = tk.IntVar()
        gender = tk.StringVar()
        self.fault = tk.StringVar()

        #==================Entry=============================
        self.full_name = tk.Entry(window, font=('arial', 10))
        lblfull_name = tk.Label(window, text = "First Name: ",bg="slategrey")
        
        self.last_name =  tk.Entry(window, font=('arial', 10))
        lbllast_name = tk.Label(window, text = "Last Name: ",bg="slategrey")
        
        self.contact_number =  tk.Entry(window, font=('arial', 10))
        lblcontact_number = tk.Label(window, text = "Contact: ",bg="slategrey")
        
        self.apartment_name =  tk.Entry(window, font=('arial', 10))
        lblapartment_name = tk.Label(window, text = "Apartment: ",bg="slategrey")
        
        self.date_of_reporting =  tk.Entry(window, font=('arial', 10))
        lbldate_of_reporting = tk.Label(window, text = "Report_Date: ",bg="slategrey")
        
        self.unit_number =  tk.Entry(window, font=('arial', 10))
        lblunit_number = tk.Label(window, text = "Unit: ",bg="slategrey")
        
        self.gender =  tk.Entry(window, font=('arial', 10))
        lblgender = tk.Label(window, text = "Gender: ",bg="slategrey")
        
        self.fault = tk.Text(window, height = 7, width = 35, font=('arial', 10))
        lblfault = tk.Label(window, text = "Fault: ",bg="slategrey")
        
        #======================Grid==================================
        self.full_name.grid(row = 0, column = 1, columnspan = 3, sticky = W+E)
        lblfull_name.grid(row = 0, column = 0)
        
        self.last_name.grid(row = 1, column = 1, columnspan = 3, sticky = W+E)
        lbllast_name.grid(row = 1, column = 0)
        
        self.contact_number.grid(row = 2, column = 1, columnspan = 3, sticky = W+E)
        lblcontact_number.grid(row = 2, column = 0)
        
        self.apartment_name.grid(row = 3, column = 1, columnspan = 3, sticky = W+E)
        lblapartment_name.grid(row = 3, column = 0)
        
        self.date_of_reporting.grid(row = 4, column = 1, columnspan = 3, sticky = W+E)
        lbldate_of_reporting.grid(row = 4, column = 0)
        
        self.unit_number.grid(row = 5, column = 1, columnspan = 3, sticky = W+E)
        lblunit_number.grid(row = 5, column = 0)
        
        self.fault.grid(row = 8, column = 1)
        lblfault.grid(row = 8, column = 0)
        #===================Buttons==================================
        style = ttk.Style(window)
        style.map('TRadiobutton', indicatorcolor=[('selected', '#00FF00')])
        Male = tk.Radiobutton(window, text="MALE", variable = gender, value = "Male").grid(row = 6, column = 1)
        Female = tk.Radiobutton(window, text="FEMALE", variable = gender, value = "Female").grid(row = 6, column = 2)
        
        
        #=====================Fuctions Validations and Insert================================
        def Insert():
            if  self.full_name.get() == "" or self.last_name.get() == "" or self.contact_number.get() == "" or self.apartment_name.get() == "" or self.date_of_reporting.get() == "" or self.unit_number.get() == "" or gender.get() == "" or self.fault.get("1.0",'end-1c') == "":
                result = tkMessageBox.showwarning('Error!', 'Please Complete The Required Field')
            else:
                tree.delete(*tree.get_children())
                conn = sqlite3.connect("FaultLoggingSystem.db")
                myCursor = conn.cursor()
                insertQry = """ INSERT INTO faultLogs 
                (FName, SName, Contact, Gender, Report_Date, Unit, AptNum, Fault)
                VALUES('{}','{}','{}','{}','{}','{}','{}','{}')
                
                """.format(self.full_name.get(), self.last_name.get(), self.contact_number.get(), gender.get(), 
                self.date_of_reporting.get(), self.unit_number.get(), self.apartment_name.get(), self.fault.get("1.0",'end-1c'))
                print(insertQry)
                myCursor.execute(insertQry)
                conn.commit()
                tkMessageBox.showinfo('Succsess', 'Imfomation is sent to Database')
                myCursor.execute("SELECT * FROM faultLogs")
                fetch = myCursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data))
                myCursor.close()
                conn.close()
                self.full_name.set("")
                self.last_name.set("")
                self.contact_number.set("")
                self.apartment_name.set("")
                self.date_of_reporting.set("")
                self.unit_number.set("")
                gender.set("")
                self.fault.set("")
        #===================Buttons==================================
        tk.Button(window, text="SUBMIT", command = Insert).grid(row = 9, column = 2)
        tk.Button(window, text = "List Fault", command = NewWindow).grid(row = 9 , column = 0)

        
class NewWindow(Toplevel):
    def __init__(self, window = None):
        super().__init__(window = window)
        self.title("List of Faults")
        self.geometry("950x200")
        self.resizable(False, False)
        self.config(bg="slategrey")
        
        
        tree = ttk.Treeview(self, column=("ID", "Name", "Surname", "Contact", "Gender", "Report Date", "Unit", "Apartment Number", "Fault"), show='headings')
        tree.column("#0", width = 10, minwidth = 5)
        tree.column( "ID", anchor = W, width = 30)
        tree.column( "Name", anchor = W, width = 120)
        tree.column( "Surname", anchor = W, width = 120)
        tree.column( "Contact", anchor = W, width = 120)
        tree.column( "Gender", anchor = W, width = 80)
        tree.column( "Report Date", anchor = W, width = 100)
        tree.column( "Unit", anchor = W, width = 30)
        tree.column( "Apartment Number", anchor = W, width = 120)
        tree.column( "Fault", anchor = W, width = 140)
        #===========Headings ======================
        tree.heading( "#0", text = "", anchor = W)
        tree.heading( "ID", text = "ID", anchor = W)
        tree.heading( "Name", text = "Name", anchor = W)
        tree.heading( "Surname", text = "Surname", anchor = W)
        tree.heading( "Contact", text = "Contact", anchor = W)
        tree.heading( "Gender", text = "Gender", anchor = W)
        tree.heading( "Report Date", text = "Report Date", anchor = W)
        tree.heading( "Unit", text = "Unit", anchor = W)
        tree.heading( "Apartment Number", text = "Apartment Number", anchor = W)
        tree.heading( "Fault", text = "Fault", anchor = W)
        
        tree.pack()
        def View():       
            conn = sqlite3.connect("FaultLoggingSystem.db")
            conn = conn.cursor()
            
            conn.execute("SELECT * FROM faultLogs")
            rows = conn.fetchall()
            
            for row in rows:
                print(row)
                tree.insert("", tk.END, values=row)
            
            conn.close()
        View()
class Database:       
    def __init__(self, window):
        conn = sqlite3.connect("FaultLoggingSystem.db")
        myCursor = conn.cursor()
        myCursor.execute("CREATE TABLE IF NOT EXISTS faultLogs (ID	INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, FName	TEXT, SName	TEXT, Contact	INTEGER, Gender	TEXT, Report_Date	DATE, Unit	INTEGER, AptNum	TEXT, Fault	TEXT)")
        conn.commit()
        conn.close()
                



window = tk.Tk()
window.title("Fault Management")
window.geometry("450x300")
window.resizable(False, False)
window.config(bg="slategrey")
faultLog = faultLog(window)
Database(window)
tree = ttk.Treeview()
window.mainloop()
