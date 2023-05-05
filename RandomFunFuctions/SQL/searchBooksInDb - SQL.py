# -*- coding: utf-8 -*-
"""
Created on Fri May 27 09:26:10 2022

@author: Yassin
"""

import sqlite3

conn = sqlite3.connect("library")
myCursor = conn.cursor()

author = input("Enter name: ")
isbn = input("Enter ISBN code: ")
book = input("Enter the Book Title: ")
edition = int(input("Book Edition: "))
rights = int(input("Copyright year: "))


sqlcTbl = "CREATE TABLE IF NOT EXISTS details(isbn TEXT, book VARCHAR(55), edition INT(20), rights INT(20), author VARCHAR(55))"
print(sqlcTbl)
myCursor.execute(sqlcTbl)
try:
    myCursor.execute(sqlcTbl)
except sqlite3.OperationalError:
    print("error in query")
    
sqlInsert = """
INSERT INTO details VALUES('{}' , '{}' , '{}' , '{}' , '{}')

""".format(isbn, book, edition, rights, author)
myCursor.execute(sqlInsert)
conn.commit()

print(sqlInsert)

sqlSelect = "SELECT * FROM details"
myCursor.execute(sqlSelect)
resultSet = myCursor.fetchall()
for row in resultSet:
    print(row)