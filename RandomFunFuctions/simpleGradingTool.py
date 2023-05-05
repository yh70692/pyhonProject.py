# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:25:11 2022

@author: Yassin
"""

myTuple = (1,2,3,4,5,6,7)

mark = int(input("Enter mark: "))

if mark >= 90:
    print("Grade A")
elif mark >= 70 and mark <= 89:
    print("Grade B")
elif mark >= 50 and mark <= 69:
    print("Grade C")
else:
    print("Less than 50% is a 'f'ail")
