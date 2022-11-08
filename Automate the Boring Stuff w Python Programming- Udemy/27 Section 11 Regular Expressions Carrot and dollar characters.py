# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:24:07 2022

@author: Zachary Mark
"""

"""
Regex
Dot Star and the Carot Dollar Characters.

Section 10
Lesson 27
"""



"""
special characters

^- string must start with the pattern
$- means the string must end with the pattern.

BOTH means the entire string must match the pattern.

"""

import re

beginsWithHelloRegex = re.compile(r'^Hello')



print(beginsWithHelloRegex.search("Hello World"))
# will return a Match Object

print(beginsWithHelloRegex.search("He Said Hello"))
#will return None



endsWithWorldRegex = re.compile(r'world!$')

print(endsWithWorldRegex.search("Hello world!"))
#will return a match object


allDigitsRegex=re.compile(r'^\d+$')
print(allDigitsRegex.search('65465465464654654'))
#will return a match object

print(allDigitsRegex.search('654654xx65464654654'))
#will not return a match object




"""

Wildcard . character.

means any character, except for new line


"""

