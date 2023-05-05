# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 09:35:42 2022

@author: Yassin Hassan
"""

import re

str='The advancements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com Then the New Yorker articale on wind farms...'

emailPattern = r'[a-z]+[0-9]*[a-z]*@[a-zA-Z]+\.com'
findMatch = re.findall(emailPattern, str)
print(findMatch)

