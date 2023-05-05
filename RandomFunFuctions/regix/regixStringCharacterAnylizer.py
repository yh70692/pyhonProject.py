# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 09:49:39 2022

@author: Yassin Hassan
"""
import re

s = "Pynative83@56#96"

def findSum(s):
    return sum(map(int, re.findall('[0-9]', s)))

average = findSum(s) / 6
high = [e for e in re.split("[^0-9]", "Pynative83@56#96") if e != '']
def findAlph(s):
    return sum(map(int,re.findall('/d+', s)))

pattern = r'[^a-zA-Z0-9\_]'
results = re.findall(pattern, (str(s)))


print("Sum is of numeric characters: ", findSum(s), "Average is ", average, "Highest is ", max(map(int, high)))
print("Sum is of Alphabetic characters: ",findAlph(s))
print("Sum is of Non alphanumeric characters: ", len(results))