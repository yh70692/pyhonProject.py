# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:39:22 2022

@author: 2cm98l3b5
"""

filename = "Writingfile.txt"
myRecord = open(filename, "a")
while True:
    
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    gross = input("Enter gross: ")
    myString = f"{name} {surname} {gross}\n"
    myRecord.write(myString)
    cont = input("Y or N : ")
    cont = cont.strip(" ").upper()
    print("You Entered : ", cont)
    if cont == "N":
        break
myRecord.close()
myRecord = open(filename, "r")
for x in myRecord:
    myList = x.split()
    #grossPay = myList[-3]
    size = len(myList)
    if size > 3:
        firstName = myList[:2]
        print(firstName[0], firstName[1])
    else:
        firstName = myList[:1]
        print(firstName[0])