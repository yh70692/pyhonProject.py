# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 21:25:47 2022

@author: Yassin
"""

import sqlite3
import sys

def mainMenu():
    print("Blood Donor Form")
    print("Select one of the following actions")
    with data:
        print("1. Register a donor")
        print("2. Display the record of all registered donors")
        print("3. Exit the program")
        print("-----------------------------")
    while True:
        try:
            mainMenu1()
            if __name__ == '__main__':
                mainMenu()
        except Exception as e:
            print(e)
            break


def mainMenu1():
    option = input("Enter an option from the menu: ")    
    if option == "1": 
        register()
    elif option == "2":
        displayRecords()
    elif option == "3":
        sys.exit()
    else:
        print("Please enter a valid number, example: 1")

def register():
    print("--------Property Registration----------")
    name = input("Enter the device name: ")
    version = input("Enter the the version: ")
    user = input("Enter username: ")
    purpose = input("Enter the purpose: ")
    with data:
        insert_property(data, table, name, version,user, purpose)
    print("\nDetails Successfully Registered\n")


def displayRecords():
    print("Displaying all registered Properties")
    with data:
        select_all_property(data, table)

def create_connection(db_file):

    data = None
    try:
        data = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
 
    return data
 
def insert_property(data, table, name, version,user, purpose):
    
    
    sql = ''' INSERT INTO '''+table+'''(name, version,user, purpose)
              VALUES(?,?,?,?,?) '''
    cur = data.cursor()
    cur.execute(sql, (name, version,user, purpose))
    data.commit()
    return cur.lastrowid


def select_all_property(data, table):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :param table:
    :return:
    """
 
    sql = ''' SELECT * FROM '''+table
    cur = data.cursor()
    cur.execute(sql)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

database = "blood_donor.db"
table = "blood_donor_info"
data = create_connection(database)
try:
    data.execute('''CREATE TABLE property_info
             (name TEXT     NOT NULL,
             version    INT  NOT NULLL,
             user   TEXT    NOT NULL,
             purpose  TEXT     NOT NULL,);''')
             
except:
    print("database already exits")
             
mainMenu()