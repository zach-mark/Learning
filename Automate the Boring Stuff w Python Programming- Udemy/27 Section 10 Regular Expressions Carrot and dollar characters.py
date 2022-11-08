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

atRegex=re.compile(r'.at')

match_list= atRegex.findall("The cat in the hat sat on the flat mat after he fled the bat.")

print(match_list)


"""
Dot Star
.* basically means anything
"""

stringy='First Name: Zach, Last Name: Mark'
nameRegex=re.compile(r'First Name: (.*), Last Name: (.*)')

listy=nameRegex.findall(stringy)
print(listy)
#that's very usefull.

#dot star is always greedy
#to use it non greedy, use a question mark after the .*:
    
#.*?
serve='<To serve humans> for dinner.>'
nongreedy= re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy=  re.compile(r'<(.*)>')
print(greedy.findall(serve))


prime="""Serve the public trust.
Protect the innocent.
Uphold the law."""


dotStar=re.compile(r'.*')

print(dotStar.search(prime))
#this will only print the first line.

dotStar=re.compile(r'.*', re.DOTALL)
#compiling this way makes the dot apply to truly everything.

print(dotStar.search(prime))


#case insensative
vowelRegex = re.compile(r'[aeiouy]', re.I)

print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))



