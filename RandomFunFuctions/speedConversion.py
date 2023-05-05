# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 10:19:15 2022

@author: Yassin
"""

def convertSpeed(mph):
	kmph =(float)(mph * 1.60934)
	return kmph


mph1 = int(input("Enter day one speed in miles/hr:" ))
mph2 = int(input("Enter two one speed in miles/hr:" ))

print("speed in day 1 km / hr is ", convertSpeed(mph1))
print("speed in day 2 km / hr is ", convertSpeed(mph2))

if mph1 == mph2:
    print("The speeds for first day and second day are all the same")
elif mph1 < mph2:
    print("The second day speed was the highest")
else:
    print("The first day speed was the highest")