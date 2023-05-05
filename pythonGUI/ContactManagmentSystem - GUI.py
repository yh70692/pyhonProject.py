# -*- coding: utf-8 -*-
"""
Created on Tue Jun 01 15:05:07 2022

@author: Yassin 
"""

from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


window = Tk()
window.title("Contact List")
window.geometry("650x350")
window.resizable(False, False)
window.config(bg="slateblue")

#============================VARIABLES===================================
first_name = StringVar()
last_name = StringVar()
gender = StringVar()
age = StringVar()
address = StringVar()
contact_number = StringVar()
first_name.set("")
last_name.set("")
gender.set("")
age.set("")
address.set("")
contact_number.set("")

class Contacts:
    def __init__(self, window):

            conn = sqlite3.connect("ContactDetails.db")
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS contact (contact_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT)")
    def NewWindow():
        global NewWin
    
        NewWin = Toplevel()
        NewWin.title("Add New Contact")
        NewWin.geometry("300x250")
        NewWin.resizable(False, False)
        NewWin.config(bg="slateblue")
        if 'UpdateWindow' in globals():
            UpdateWindow.destroy()
        
        #===================FRAMES==============================
        FormTitle = Frame(NewWin)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(NewWin)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm)
        Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male",  font=('arial', 10)).pack(side=LEFT)
        Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female",  font=('arial', 10)).pack(side=LEFT)
        
        #===================LABELS==============================
        lbl_title = Label(FormTitle, text="Add Contact", font=('arial', 12), bg="green",  width = 300)
        lbl_title.pack(fill=X)
        lbl_firstname = Label(ContactForm, text="Firstname", font=('arial', 10), bd=5)
        lbl_firstname.grid(row=0, sticky=W)
        lbl_lastname = Label(ContactForm, text="Lastname", font=('arial', 10), bd=5)
        lbl_lastname.grid(row=1, sticky=W)
        lbl_gender = Label(ContactForm, text="Gender", font=('arial', 10), bd=5)
        lbl_gender.grid(row=2, sticky=W)
        lbl_age = Label(ContactForm, text="Age", font=('arial', 10), bd=5)
        lbl_age.grid(row=3, sticky=W)
        lbl_address = Label(ContactForm, text="Address", font=('arial', 10), bd=5)
        lbl_address.grid(row=4, sticky=W)
        lbl_contact = Label(ContactForm, text="Contact", font=('arial', 10), bd=5)
        lbl_contact.grid(row=5, sticky=W)
    
        #===================ENTRY===============================
        firstname = Entry(ContactForm, textvariable= first_name , font=('arial', 10))
        firstname.grid(row=0, column=1)
        lastname = Entry(ContactForm, textvariable= last_name , font=('arial', 10))
        lastname.grid(row=1, column=1)
        RadioGroup.grid(row=2, column=1)
        age1 = Entry(ContactForm, textvariable= age,  font=('arial', 10))
        age1.grid(row=3, column=1)
        address1 = Entry(ContactForm, textvariable= address,  font=('arial', 10))
        address1.grid(row=4, column=1)
        contact = Entry(ContactForm, textvariable= contact_number ,  font=('arial', 10))
        contact.grid(row=5, column=1)
        
    
        #==================BUTTONS==============================
        btn_addcon = Button(ContactForm, text="Save", width=10, command=Contacts.Submit )
        btn_addcon.grid(row=6, columnspan=2, pady=10)
       
    
    def Delete():
        if not tree.selection():
           result = tkMessageBox.showwarning('Error!', 'Please Select A Contact First!')
        else:
            result = tkMessageBox.askquestion('Are you sure?', 'Do you want to delete this contact?')
            if result == 'yes':
                curItem = tree.focus()
                contents =(tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                conn = sqlite3.connect("ContactDetails.db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM contant WHERE contact_id = %d" % selecteditem[0])
                conn.commit()
                cursor.close()
                conn.close()
    def Submit():
        if  first_name.get() == "" or last_name.get() == "" or gender.get() == "" or age.get() == "" or address.get() == "" or contact_number.get() == "":
            result = tkMessageBox.showwarning('Error!', 'Please Complete The Required Field')
        else:
            tree.delete(*tree.get_children())
            conn = sqlite3.connect("ContactDetails.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO contact (firstname, lastname, gender, age, address, contact) VALUES(?, ?, ?, ?, ?, ?)", (str(first_name.get()), str(last_name.get()), str(gender.get()), int(age.get()), str(address.get()), str(contact_number.get())))
            conn.commit()
            cursor.execute("SELECT * FROM contact ORDER BY lastname ASC")
            fetch = cursor.fetchall() 
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            first_name.set("")
            last_name.set("")
            gender.set("")
            age.set("")
            address.set("")
            contact_number.set("")   
    def Update(self):
        if gender.get() == "":
           result = tkMessageBox.showwarning('Error!', 'Please Complete The Required Field')
        else:
            tree.delete(*tree.get_children())
            conn = sqlite3.connect("ContactDetails.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE `contact` SET `firstname` = ?, `lastname` = ?, `gender` =?, `age` = ?,  `address` = ?, `contact` = ? WHERE `contact_id` = ?", (str(first_name.get()), str(last_name.get()), str(gender.get()), str(age.get()), str(address.get()), str(contact_number.get()), int(contact_id)))
            conn.commit()
            cursor.execute("SELECT * FROM contact ORDER BY lastname ASC")
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            first_name.set("")
            last_name.set("")
            gender.set("")
            age.set("")
            address.set("")
            contact_number.set("")
             


#============================FRAMES======================================
Top = Frame(window, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(window, width=500,  bg="slateblue")
Mid.pack(side=TOP)

MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="slateblue")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(window, width=500)
TableMargin.pack(side=TOP)
#============================LABELS======================================
title = Label(Top, text="Contact Management System",bg = "silver",  width=500).pack(fill=X)

#============================ENTRY=======================================

#============================BUTTONS=====================================
add = Button(MidLeft, text="ADD NEW", command=Contacts.NewWindow).pack()
delete = Button(MidRight, text="DELETE", command=Contacts.Delete).pack(side=RIGHT)

#============================TABLES======================================

tree = ttk.Treeview(TableMargin, columns=("ID", "Firstname", "Lastname", "Gender", "Age", "Address", "Contact"), height=400, selectmode="extended")

tree.heading('ID', text="ID", anchor=W)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Age', text="Age", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Contact', text="Contact", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
#============================FRAMES======================================

#============================ENTRY=======================================
conn = sqlite3.connect("ContactDetails.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM contact ORDER BY lastname ASC")
fetch = cursor.fetchall()
for data in fetch:
    tree.insert('', 'end', values=(data))
cursor.close()
conn.close()
#============================BUTTONS=====================================

window.mainloop()
