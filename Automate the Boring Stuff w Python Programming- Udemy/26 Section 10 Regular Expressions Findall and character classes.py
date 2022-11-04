# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:11:01 2022

@author: Zachary Mark
"""

"""
Section 10- Regular Expressions

Lesson 26- Findall and regex character classes
"""

import re


phoneRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

text_to_search="my numbers are 555-555-1234, 555-555-0011, 555-555-9999."


#regular search
print(phoneRegex.search(text_to_search)) #gives a match object

#vs

#findall search

print(phoneRegex.findall(text_to_search)) #gives a list of numbers



#FIND ALL behaves differently with groups.

phoneRegex= re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

print(phoneRegex.findall(text_to_search)) #gives a list of touples, with each group in a touple field








"""
character classes
"""

"""
\d- any numeric digit
we could also go the stupid long way and used pipes r'(0|1|2|3|4|5|6|7|8|9)


other classes:
\d- any numeric digit
\D- any character that is not a digit
\w- any letter, digit or underscore
\W- anything not a letter, digit, or underscore
\s- any space, tab or newline
\S- any character that is not a space, tab, or newline
"""


#12 days of christmas example

lyrics=" 12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree"


xmasRegex=re.compile(r'\d+ \w+')

twelvedays=xmasRegex.findall(lyrics)

for i in twelvedays:
    print(i)


"""
Making your own classes
"""
vowelRegex = re.compile(r'[aeiouyAEIOUY]') #same as r'(a|e|i|o|u|y)'

test_string="Robocop eats baby food."

print(vowelRegex.findall(test_string))

alllowerRegex = re.compile(r'[a-z]')

allLettersRegex = re.compile(r'[a-zA-Z]')


doublevowerRegex=re.compile(r'[aeiouyAEIOUY]{2}')

#a carrot will find anything not in that group

novowelsRegex = re.compile(r'[^aeiouyAEIOUY]')

print(novowelsRegex.findall(test_string))


