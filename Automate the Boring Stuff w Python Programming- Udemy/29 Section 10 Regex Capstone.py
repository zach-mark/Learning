#! python3


"""
Created on Tue Nov  8 18:28:49 2022

@author: Zachary Mark
"""


"""
Section 10

Lesson 29: Regex capstone- a phone and email scraper


How to go through documents and grab numerous 
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


? - 0 or 1
* - 0 or more
+ - 1 or more

"""

import re, pyperclip

#create regex for phone numbers

phone_Regex=re.compile(r"""
                       #555-555-5555, (555)-555-5555, 555-5555, 555-555-5555 ext 12345, ext. 12345, x12345, x 12345
                       (
                       ((\d\d\d) | (\(\d\d\d\)))?           #area code (optional)
                       (\s | - | \.)?                       #first separator
                       \d\d\d                               #first 3 digits
                       (\s | - | \.)                        #separator
                       \d\d\d\d                             #last 4 digits
                       
                                                            #begin extension part                       
                       (
                       ((ext(\.)?\s|x(\s)?))                #extension word part
                       (\d{2,5})                            #extension number part
                       )?    
                       )
                       """, re.VERBOSE)


#create regex for email addresses
email_Regex=re.compile(r"""
                       
                       #something@something.com
                       #something.zoob@something.com
                       
                       #name part
                       [a-zA-Z0-9_.+]+                      #can't use \w checks for identifier in email
                       @                                    #checks for @, very simple
                       [a-zA-Z0-9_.+]+                      #checks for domain name
                       """, re.VERBOSE)


#get text off the clipboard
text=pyperclip.paste()

#extract email and phone from the text

phone_numbers=phone_Regex.findall(text)
found_numbers=[]
for entry in phone_numbers:
    found_numbers.append(entry[0])

emails=email_Regex.findall(text)

#copy the extracted email/phone to the clipboard



phone_number_string='\n'.join(found_numbers)


email_string='\n'.join(emails)

results= phone_number_string + " " + email_string

print(results)

pyperclip.copy(results)