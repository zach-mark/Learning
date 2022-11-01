# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:01:21 2022

@author: Zachary Mark
"""



"""
Section 8 More about Strings 
Video 20 String Methods
AND VIDEO 21- Formating (so quick and low info, didn't need its own file')
"""


spam="Hello World"
print(spam.upper())
#upper makes everything uper case

#Strings are immutable, so to change the variable, it would be:
    
spam=spam.upper()
spam=spam.lower()
#lower- self explanitory
print(spam)


#islower()
#isupper

#check if the whole string is upper or lower

"""
Other cool functions:
    isalpha()- check if letters only
    isalnum()- check if numbers and letters only
    isdecimal()- numbers only
    isspace()- whitespace only
    istitle()- titlecase only "Hello World" example
    """

"""
MORE cool functions:
    startswith('Hello')- are the first characters in the string, this?
    endswith("World!")
    
    """

#JOIN()

print(', '.join(['cats','rats','bats']))
#join uses the called string as the separator. pretty heckin cool.

#Split()

spam="Hello World"
spam=spam.split() #returns a list. defaults to space as the spliter. other strings can be fed as arguments
print(spam)


#rjust and ljust

print('hello'.rjust(50, "*"))

print('hello'.center(50, "*"))

#strip


spam='hell oooo worldooo'

print(spam.strip())

spam="spamspamspamspamspamspamZacharyspamspamspam"

print(spam.strip("spam"))


"""
String Formating
"""

name='Zach'
place='School'
time= '6pm'
food='Turnips'

print("Hello "+ name +", you are invited to a party at "+place+" at "+ time+ ". Please bring "+ food+".")

#A better method

string= "Hello %s, you are invited to a party at %s at %s. Please Bring %s." % (name, place, time, food)
print(string)

# %S, very powerful