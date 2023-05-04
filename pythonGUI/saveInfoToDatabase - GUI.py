# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 09:53:18 2022

@author: 2cm98l3b5
"""

import tkinter as tk
import sqlite3

window = tk.Tk()
window.title("Enter Student Infomation To Save To Database")
window.geometry("400x200")
window.resizable(False, False)

txtName = tk.StringVar()
txtNum = tk.StringVar()
txtMod = tk.IntVar()

lblName = tk.Label(window, text = "Student Name: ")
lblNum = tk.Label(window, text = "Student Number: ")
lblMod = tk.Label(window, text = "Student Module: ")
        
txtName = tk.Entry(window)
txtNum = tk.Entry(window)
txtMod = tk.Entry(window)

buttonSubmit = tk.Button(window,text = "Save to Database" ,command = lambda: Insert())
        
lblName.grid(row = 1, column = 3,columnspan=4)
lblNum.grid(row = 3, column = 3,columnspan=4)
lblMod.grid(row = 5, column = 3,columnspan=4)
        
txtName.grid(row = 2, column = 3,columnspan=4)
txtNum.grid(row = 4, column = 3,columnspan=4)
txtMod.grid(row = 6, column = 3,columnspan=4)

buttonSubmit.grid(row = 7, column = 3,columnspan=4) 


def Insert():
    conn = sqlite3.connect("exam.db")
    conn = conn.cursor()
    insertQry = """ INSERT INTO studentDetails 
    (Name, Student_Number, Module)
    VALUES('{}','{}','{}')
    
    """.format(txtName.get(),txtNum.get(),txtMod.get())
    print(insertQry)
    conn.execute(insertQry)
    conn.commit()

def database():
    conn = sqlite3.connect("exam.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS studentDetails (ID	INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, Name	TEXT, Student_Number	INTEGER, Module	VARCHAR)")
    conn.commit()
    #conn.close()



database()
window.mainloop()