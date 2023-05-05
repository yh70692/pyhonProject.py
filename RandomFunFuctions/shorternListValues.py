# -*- coding: utf-8 -*-
"""
Created on Fri May 27 08:15:55 2022

@author: Yassin
"""

weekDays = ["Monday" , "Tuesday", "Wendsday", "Thursday", "Friday", "Sateday", "Sunday"]

for days in weekDays:
    weekDays[:] = (days[:3] for days in weekDays)

print(weekDays)
    