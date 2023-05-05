# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 08:45:54 2022

@author: Yassin
"""
import tkinter as tk

class myfirstGUI:
    def __init__(self, window):
        self.myAnswer = tk.StringVar()
        self.txtName = tk.StringVar()
        self.txtSur = tk.StringVar()
        
        self.lblName = tk.Label(window, text = "Enter Name: ")
        self.lblSur = tk.Label(window, text = "Enter Surname: ")
        
        self.txtName = tk.Entry(window)
        self.txtSur = tk.Entry(window)
        
        self.lblAnswer = tk.Label(window, textvariable = self.myAnswer)
        self.buttonSubmit = tk.Button(window,text = "Submit" ,command = self.addDetails)    
        self.btnCancel = tk.Button(window,text = "Cancel", command = self.clearDetails)
        
        self.lblName.grid(row = 0, column = 0,sticky="ns")
        self.lblSur.grid(row = 1, column = 0,sticky="ns")
        
        self.txtName.grid(row = 0, column = 1,sticky="ns")
        self.txtSur.grid(row = 1, column = 1,sticky="ns")
        
        self.lblAnswer.grid(row = 2, column = 0)
        self.buttonSubmit.grid(row = 3, column = 0) 
        self.btnCancel.grid(row = 3, column = 1) 

    def addDetails(self):
        myString = "Your Info"+ "\nName: "+ self.txtName.get() + "\nSurname: " + self.txtSur.get()
        self.myAnswer.set(myString)

        
    def clearDetails(self):
        pass
    
myWindow = tk.Tk()
myGUI = myfirstGUI(myWindow)
myWindow.mainloop()

