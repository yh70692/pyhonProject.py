# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:55:32 2022

@author: Yassin
"""


class UnderscorePrefix:
    def __init__(self) -> None:
        # Using _ suffice to declare private variables
        self._name = "Caleb"

class UnderscoreSuffix:
    class_ = "Peter"

class Ignore:
    # Is the underscore called Throw-Way-Variable?
    # Seems to be called ignore
    for _ in range(3):
        print("Mirror")

sing = UnderscorePrefix()
print(sing._name)
# When do we get to use reserved words as variables.
print(UnderscoreSuffix.class_)



