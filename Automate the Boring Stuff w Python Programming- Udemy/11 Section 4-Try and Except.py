"""
Created on Wed Oct 26 19:54:41 2022

@author: Zachary Mark

Try and Except Statements

Errors will crash programs, without try except statements
"""

#forcing an error

def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print("You tried to divide by zero")
        
"""
except can work by itself, or with a specific error called out
"""

print((div42by(2)))
print((div42by(12)))
print((div42by(0))) #try prevents the error
print((div42by(1)))


print()
print()
"""
number of cats example
"""

print("How many cats do you have?")
cats=numCats=input()
try:
    if int(cats) >=4:
        print("WOW! lots of cats.")
    elif int(cats)<0:
        print("thats not possible.")
    else:
        print("Thats not many cats...")
except ValueError:
    print('that is not a number?')