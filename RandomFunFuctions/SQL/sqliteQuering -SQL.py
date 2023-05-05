# -*- coding: utf-8 -*-
"""
Created on Fri May 27 09:37:41 2022

@author: Yassin
"""

import sqlite3

conn = sqlite3.connect("library")
myCursor = conn.cursor()

#1
sqlselect1 = "SELECT * FROM details WHERE rights == 2009;"
myCursor.execute(sqlselect1)
result1 = myCursor.fetchall()
print(result1)
print("--------------------------------")
#2
sqlselect2 = "SELECT book FROM details ORDER BY book ASC;"
myCursor.execute(sqlselect2)
result2 = myCursor.fetchall()
print(result2)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#3
sqlselect3 = "SELECT isbn, author FROM details;"
myCursor.execute(sqlselect3)
result3 = myCursor.fetchall()
print(result3)
print("--------------------------------")
#4
sqlselect4 = "SELECT * FROM details WHERE book LIKE '[!c]%';"
myCursor.execute(sqlselect4)
result4 = myCursor.fetchall()
print(result4)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
