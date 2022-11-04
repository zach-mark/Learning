# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:25:50 2022

@author: Zachary Mark
"""


"""
23 Regular Expression
Basics
"""


def isPhoneNumber(text):
    text_len=len(text)
    
    if text_len not in [10,12]:
        return False #not phone number sized
    
    if text_len==12:
        for i in range(0,3):
            if not text[i].isdecimal():
                return False #no area code or insufficent nubmers
        
        if text[3] not in ['.','-',' ']:
            return False #missing dash, and not correct len to have no dash
        
        
        for i in range(4,7):
            if not text[i].isdecimal():
                return False #not nubmers
            
        if text[7] not in ['.','-',' ']:
            return False #missing dash, and not correct len to have no dash
            
        
        
            
        for i in range(8,12):
            if not text[i].isdecimal():
                return False #not nubmers
    else:
        
        for i in range(0,10):
            if not text[i].isdecimal():
                return False #not nubmers
    
    return True

def check_message_for_numbers(text):
    message=text
    found_number=[]
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print("PhoneNumberFound: "+ chunk)
            found_number.append(chunk)
    
    return found_number


#alt method, using the RE module
import re

message="call me tomorrrow at 231-571-5116. or my office at 216-555-1234"

phoneNumRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.findall(message)
print(mo)