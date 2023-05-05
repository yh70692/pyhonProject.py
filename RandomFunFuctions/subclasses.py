# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:57:36 2022

@author: Yassin
"""

class Vehicle:
    model = None
    country = 0
    def __init__(self,engine , make , model):
         self.engine = "3L"
         self.model = "sedan"
         self.make = "toyota"


class Car(Vehicle):
    def __init__(self):
        self.engine = "2L"
        self.model = "M5"
        self.make = "BMW"
        
G = Car()
print(G.engine)
print(G.model)
print(G.make)