# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:54:07 2022

@author: Yassin
"""

from tkinter import *


def focus1(event):
    nameFile_field.focus_set()


def focus2(event):
    content_field.focus_set()


def clear():
    nameFile_field.delete(0, END)
    content_field.delete(1.0, "end-1c")


def insert():
    if(nameFile_field.get() == "" and content_field.get() == ""):
        print("Empty Input")
    else:
        with open(nameFile_field.get(), 'w') as f:
            f.write(content_field.get(1.0, "end-1c"))

    clear()


if __name__ == "__main__":
    root = Tk()
    root.configure(background="light grey")

    root.title("GUI and File Handeling")
    root.geometry("500x400")

    heading = Label(root, text="", bg="light grey")

    nameFile = Label(root, text="Enter the File Name", bg="light grey")
    nameFile1 = Label(root, text="Enter File Contents", bg="light grey")
    content = Label(root, text="", bg="light grey")

    heading.grid(row=0, column=1)
    nameFile.grid(row=1, column=0)
    nameFile1.grid(row=3, column=1)
    content.grid(row=2, column=0)

    nameFile_field = Entry(root)
    content_field = Text(root, height=15, width=20)

    nameFile_field.bind("<Return>", focus1)
    content_field.bind("<Return>", focus2)

    nameFile_field.grid(row=1, column=1, ipadx="100")
    content_field.grid(row=4, column=1, ipadx="100")

    submit = Button(root, text="Save The File", fg="Black", bg="light grey", command=insert)
    submit.grid(row=9, column=1)

    # start the GUI
root.mainloop()