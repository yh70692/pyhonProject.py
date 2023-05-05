# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 07:47:56 2022

@author: Yassin
"""
import re

# creating an empty list
lst = []
    
def insert():
    # number of elements as input
    n = int(input("Enter number of elements : "))
      
    # iterating till the range
    for i in range(0, n):
        ele = str(input())
      
        lst.append(ele) # adding the element
      
    print(lst)
    
def search():
    match = str(input("Enter the name you want to search? : "))
    findMatch = re.findall(match, str(lst))
    if  match in str(lst):
        print("Name found.")
        print(findMatch)
        for match in enumerate(lst): 
            print ("Index position:", match)
    else:
        print("Name not found.")

def replace():
    name = input("Enter the name you want to change. : ")
    if name in lst:
      i = lst.index(name)  
    
      new = input("Enter new name: ")
      lst[i] = new
    else:
      print("Name is not in the list.")
    print(lst)


insert()
search()
replace()