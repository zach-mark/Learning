
"""
Section 3- Video 9

Writing My Own Functions
"""

"""
Good website for reference when trying to understand code as it executes
    https://pythontutor.com/
"""


def hello(name): #defines a function with the name parameter
    print("Howdy!")
    print("Howdy!!!")
    print("Hello There, "+ name+ "!")
    #function ends after the indent.
    
    
hello("Alice") #this calls the defined function, with "Alice" as the argument

hello("Bob") #this does it again, but with "Bob"



def plusOne(number):
    
    return number+1


newNumber=plusOne(2)
print(newNumber)



"""
If a function doesn't have a return value,
it defaults to "None" as the value
"""

print("hello", end='') #modifies using the keyword arguments
                        #to use '' instead of '\n'
print("World")

print("cat","dog","mouse", sep="~~")
#Keyword arguments are typically optional when using functions.

