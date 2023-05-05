# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:39:37 2022

@author: Yassin
"""

def PrintNumbers(height: int):
    for row in range(1, height + 1):
        for column in range(1, row + 1):
            print(column, end = "")
        print("")

def PrintStars(height: int):
    for row in range(1, height + 1):
        for column in range(1, row + 1):
            print("*", end = "")
        print("")

PrintStars(10)
PrintNumbers(10)