# -*- coding: utf-8 -*-
"""
Created on Thu May 19 08:39:20 2022

@author: Yassin
"""
#
def addDetails(message):
    value = input(message)
    return value
#area 
def calcArea(length,height):
    area = length / height
    return area

def showDetails(name):
    print("My name is", name , "I will assist with the math you give me your details.")

print("Calculate your area! can be your body or your house measurements")
    
showDetails("AreaCalc")
# trapping the errors
while True:
    try:
        length = int(addDetails("Enter the length: "))
        print(length)
        height = int(addDetails("Enter the height: "))
        
    except ValueError:
        print("Captured values are not accept")
    except ZeroDivisionError:
        print("Height cannot be zero")
    else:
        #area = calcArea(length, height)
        print("The area is: ", calcArea(length,height))
        break
        