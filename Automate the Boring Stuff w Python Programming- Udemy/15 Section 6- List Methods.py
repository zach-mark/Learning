# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:36:51 2022

@author: Zachary Mark
"""
"""
Lesson 15
Section 6
List Methods
"""


spam=['hello', 'hi', 'howdy', 'greetings', 'hey']
#make a list

print(spam.index('hi'))
print(spam.index('hey'))
#index tells you where in the list the value is, starting from 0
#will return ValueError if not in the list
#if the value is in the list 2+ times, it will return the first index position


spam=['cat', 'dog', 'bat']

#append, adds to the end
spam.append('mouse')

#insert adds to the selected index
spam.insert(1,'moose')


#remove and pop

spam.remove('moose')
#remove removes the first instance of the stated value

spam.pop(2)
#removes info from the list, based on the index provided, rather than searching for a value
#pop returns the value as well, very useful.


spam=[2,55,12,15,11,45]
spam.sort()
print(spam)

spam=[100,112,151,162]
spam.sort(reverse=True)
print(spam)
#sort is pretty simple... sorts accending unless a value passed (reverse=True)
#uses 'ASCIbetical' order, not alpha. Uppercase letters come first. Uppercase Z is before lowercase a.
#this is fixed using the keyword 'key=str.lower'


