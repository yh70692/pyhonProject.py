# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:17:50 2022

@author: Yassin
"""


import random

randomList = [1,2,3,4,5]

print("If you are lucky you will pay only 40% of your total payment.")
name = input("Enter your name: ")
pay  = int(input("\n Enter the amount pay: "))
inNum = int(input("\n Please enter Invoice number: "))


if inNum == randomList[3]:
    print(name,"it is your lucky day, the amount to pay for invoice",inNum,"is",pay,"Thanks for shopping with us")
else:
    print("Sorry,",name ,"No luck today, the amount to pay for invoice",inNum,"is", pay,"Thanks for shopping with us")