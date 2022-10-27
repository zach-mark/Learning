# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:47:23 2022

@author: Zachary Mark
"""

"""
Lesson 16
Section 6

Similarities Between Lists and Strings
"""

#easily converted from a string to a list using list()
#can easily use indexing and slicing.
#lists are mutable, strings are immutable

#cant assign a letter in a string
#have to make new strings if you want to modify strings


"""
IMPORTANT- BUGS WILL OCCUR IF YOU DONT UNDERSTAND
"""

spam=[0,1,2,3,4]
cheese=spam #this does not clone spam, it makes a secondary reference to spam

cheese[1]="dog"

print(spam)
print(cheese)

#these will be the same.

def eggs(something):
    something.append('Hello')
    #changes made in the fuction to the global variable spam, will be stored externally
    
spam=[1,2,3]
eggs(spam)
print(spam)

#THE WORKAROUND IS the COPY module
print('#### Learning Copy')
import copy

spam=[1,2,3,4,5]
cheese=copy.deepcopy(spam)
cheese[1]="eggs"

print(spam)
print(cheese)


#last, good to know, the "\" symbol carries the line to the next

print(1+2+\
      333)