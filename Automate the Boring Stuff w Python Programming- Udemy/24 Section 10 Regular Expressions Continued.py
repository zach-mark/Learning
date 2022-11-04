# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:46:59 2022

@author: Zachary Mark
"""

"""
24 Regular Expression
Groups and the Pipe Character
"""

import re

phoneNumber_regex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

message= "My number is 555-555-1234"

mo= phoneNumber_regex.search(message)
print(mo.group())




phoneNumber_regex= re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo= phoneNumber_regex.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))



#the pipe character |

bat_regex= re.compile(r'Bat(man|mobile|copter|bat)')

message= "Batmobile lost a wheel and the joker got away"

mo=bat_regex.search(message)

print(mo.group())
print(mo.group(1))