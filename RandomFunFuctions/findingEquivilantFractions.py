"""
Created on Fri Jun 24 11:27:14 2022

@author: AKiba2x0
"""
class Fraction:
    def __init__(self):
        
        denominator = ""
        numerator = ""
        denominator2 = ""
        numerator2 = "" 
        
        print("Enter the 1st Fraction.")
        numerator = int(input("The numerator : "))
        denominator = int(input("The denominator : "))
        
        print("===============")
        
        print("\nEnter the 2nd Fraction.")
        numerator2 = int(input("The numerator: "))
        denominator2 = int(input("The denominator: "))

        first = numerator * denominator2
        second = numerator2 * denominator
        bothD = denominator * denominator2

        totalTop = first + second
        totalBottom = bothD
        print("\n===============")
        print("The equivalant for the fractions are: \n",totalTop,"/",totalBottom)
        

Fraction()