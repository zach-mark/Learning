# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:06:32 2022

@author: Zachary Mark

Section 5, Guess the number game!
"""
#guess the number game

import random
print("Hello, what is your name?")

name=input()

secretNumber=random.randint(1,100)

if name=="DEBUG":
    print("DEBUG: Secret number is "+str(secretNumber))

print("Hi "+str(name)+", I am thinking of a number between 1, and 100, can you guess it?")

guesses=10
guesses_taken=0

while guesses>0:
    print("take a guess!")
    guess=int(input())
    guesses_taken+=1
    if guess< secretNumber:
        print("your guess is too low!")
    elif guess> secretNumber:
        print("your guess is too high!")
        
    else:
        break
    guesses-=1
if guess==secretNumber:
    
    print("Way to go, you guessed the number! You got the number in "+str(guesses_taken)+" guesses!")
else:
    print("Sorry, "+name+" you're out of guesses... The secret number was "+str(secretNumber))
    
