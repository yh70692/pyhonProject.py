# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 07:57:13 2022

@author: Yassin
"""
import tkinter as tk


class TextFile:
    def __init__(self, window):
        
        self.box = tk.Listbox(window, height = 12, width = 40)
        self.box.grid(row = 2, column = 0, columnspan = 3)

        
        popbtn = tk.Button(window, text = "Populate", command = self.populate).grid(row = 0, column = 0)
        
        clearbtn = tk.Button(window, text = "Clear", command = self.clear).grid(row = 0, column = 1)

        
    def populate(self):
        openFile = open("myDetails.txt", "r")
        
        for txt in openFile:
            self.box.insert("end", txt)
            print(txt)
        openFile.close()

    
    def clear(self):
        self.box.delete(0, "end")


def main():
    window = tk.Tk()
    window.title('Display a Text File')
    window.resizable(False, False)
    window.geometry('300x300')
    file = TextFile(window)
    window.mainloop()

main()