# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 17:05:55 2022

@author: Zachary Mark
"""


"""
Lesson 17
Section 7

Dictionary Data Type
"""

"""

"""

#example_dict
myCat={'size'       : 'fat',
       'color'      : 'gray',
       'disposition': 'loud'}
#dictionaries stored in variables.
#myCat is the variable
#information indexes are called keys. keys are accessed through their keys
#example:
print('my cat has '+myCat['color']+' fur')


#[1,2,3]!=[2,1,3]
#{'Pickle','HotDog'}=={'HotDog','Pickle'}
#items in dictionaries are unordered. Order matters in lists, not dicts.


#check if something is in dictionary?
if 'size' in myCat:
    print('true')

#dictionary methods
#keys(), values(), and items()
#use with list to get the info
#they return list like data types.



#get() method, V important

eggs={'color': 'yellow',
      'type': 'sunnyside'}

#get will return if the key is in the dict, but if not, returns the 2nd argument.
#wish I knew this a year ago.
print(eggs.get('type',0))
print(eggs.get('cheese',0))

#set default, will check if the key exists, and then will change it if not
