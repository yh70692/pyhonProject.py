# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:29:40 2022

@author: Yassin
"""
myList = []

n = int(input("Enter number of names: "))
print("Enter the names")

for i in range(n):
    myList.append(input())

searchbar = input("Enter the name to search: ")
if searchbar in myList:
  print("Position of name is",myList.index(searchbar))
else:
  print("Name not found in list")

searchbar = input("Enter the name to change: ")
if searchbar in myList:
  p = myList.index(searchbar)  

  checker = input("Enter new name: ")
  myList[p] = checker  
else:
  print("Name not found in list")

myList.sort()
#print name in order from small to big order
print("Names in Ascending order")
for i in myList:
  print(i)
print()# print Statement
#sort list in descending order
myList.sort(reverse = True)
#print names
print("Names in Descending order")
for i in myList:
  print(i)