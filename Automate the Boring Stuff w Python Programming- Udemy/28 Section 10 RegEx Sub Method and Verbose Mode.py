# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:11:28 2022

@author: Zachary Mark
"""

"""
Section 10

Lesson 28- Regex Sub() Method and Verbose Mode

"""

import re

agentRegex=re.compile(r'Agent \w+')

string="Agent Alice gave the top secret documents to Agent Bob. Agent Molder still has the flash drive."


print(agentRegex.findall(string))

"""
the sub method, serves as a type of find and replace
"""
print(agentRegex.sub("REDACTED", string))





agentRegex=re.compile(r'Agent (\w)\w*')

print(agentRegex.findall(string))
#this will find all the agent's first initials

#the \1 will pull from the first group in a regex match
print(agentRegex.sub(r"Agent \1*****", string))



"""
Verbose Mode
"""

phone_number_RegEx=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

print(phone_number_RegEx.findall("999-999-9959"))

#a better alternative:
    
verbose_phone_regex=re.compile(r"""
                                \d\d\d    #Area code. I can comment here in the string. dope
                                -         # first dash
                                \d\d\d    #first 3 digits
                                -         #second dash
                                \d\d\d\d  #last 4 digits
                                """, re.VERBOSE)


print(verbose_phone_regex.findall("555-555-5515, 444-555-6666, 222-51-4455"))


#other arguments that can be passed to compile

"""
re.DOTALL
re.VERBOSE
re.IGNORECASE
etc.

To use them together, the syntax:
"""
re.compile(r'/d/d/d', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# this is called a bitwise "OR" operator. outside scope of this course.



















