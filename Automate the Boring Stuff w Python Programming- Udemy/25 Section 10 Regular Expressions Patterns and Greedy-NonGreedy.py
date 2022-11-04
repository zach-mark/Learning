# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:48:27 2022

@author: Zachary Mark
"""

"""
Section 10- Regular Expressions

Lesson 25- Repetition in Regex Patterns and Greedy/Nongreedy Matching

"""

import re

"""
?
"""
batRegex = re.compile(r'Bat(wo)?man') #the question mark indicates that the wo group can be in the string 0 or 1 times

mo=batRegex.search("the Adventures of Batman")

if mo!=None:
    print(mo.group())

"""
*
"""
batRegex = re.compile(r'Bat(wo)*man') #the astricks indicates that the wo group can be in the string 0 or more times

mo=batRegex.search("the Adventures of Batwowowowowowowowowoman")

if mo!=None:
    print(mo.group())

"""
+
"""

batRegex = re.compile(r'Bat(wo)+man') #the plus indicates that the wo group must be in the string 1 or more times

mo=batRegex.search("the Adventures of Batman")#will return none

if mo!=None:
    print(mo.group())


mo=batRegex.search("the Adventures of Batwowowoman")#will return a match

if mo!=None:
    print(mo.group())

"""
To recap

? - 0 or 1
* - 0 or more
+ - 1 or more

"""

haRegex = re.compile(r'(ha){3}')
print(haRegex.search('He said hahahahahaahahahaha'))




haRegex=re.compile(r'(ha){3,5}') #this will look for between 3 and 5 ha's in a row

haRegex=re.compile(r'(ha){3,}') #this will look for 3 or more ha's in a row


#regular expressions default to greedy, they will atttempt to match the longest possible string.

#a questionmark after the curly brace will look for a non greedy match

digitRegex_greed=re.compile(r'(\d){3,}')
digitRegex_nongreed=re.compile(r'(\d){3,}?')

print(digitRegex_greed.search('1234567890'))
print(digitRegex_nongreed.search('1234567890'))