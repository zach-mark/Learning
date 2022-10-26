"""
Created on Wed Oct 26 16:54:41 2022

@author: Zachary Mark
"""

"""
Python's Built in Functions
"""
#print("Hello World")
#len("words")


"""
Module Functions
"""
#import random

#a=random.randint(0,22)
#print(a)

#both import and random work
#but 'from' 'import *' means I don't have to use the module name when calling functions
#from random import *

#a=randint(0,22)
#print(a)

#import sys
#print('hello')
#sys.exit()
#print('goodbye') #this

"""
3rd party functions

use 'pip install MODULE' to add the module to my available modules
"""
#'pip install pyperclip'
import pyperclip
pyperclip.copy('Hello world!') #adds text to the clipboard! VERY VERY COOL
a=pyperclip.paste()

print(a)






#Global and Local Scopes