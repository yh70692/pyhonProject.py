# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:49:50 2022

@author: Yassin
"""

import threading
import time

def PrintNumbers(height: int):
    for row in range(1, height + 1):
        for column in range(1, row + 1):
            print(column, end = "")
        print("")
        time.sleep(3)

def PrintStars(height: int):
    for row in range(1, height + 1):
        for column in range(1, row + 1):
            print("*", end = "")
        print("")
        time.sleep(3)

# How to creat a thread:
# thread = threading.Thread(target = PrintNumbers, args = 5(We use args for passing argument))
firstThread = threading.Thread(target = PrintNumbers, args = [5])
secondThread = threading.Thread(target = PrintStars, args = [4])
#A thread is in many sates, its alive , sorted or dead
begin = time.perf_counter()
firstThread.start()
# Join() does not let each thread finish before it takes another
#firstThread.join()

secondThread.start()
secondThread.join()

end = time.perf_counter()
duration = end - begin

print(f"The thread took {duration} seconds.")