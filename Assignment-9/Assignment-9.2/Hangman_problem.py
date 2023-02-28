# Assignment 9.2 - Hangman problem

import random
import time
print ("Welcome to hangman game!")

with open('data.txt') as f:
    lst = [line.rstrip() for line in f]

rand_idx = random.randrange(len(lst))
word = lst[rand_idx]
print ("Start guessing...")
guesses = ''
turns = 6
while turns > 0:         

    failed = 0                
    for char in word:      
        if char in guesses:    
            print (char,end=""),    

        else:
            print (" _ ",end=""),     
            failed += 1    
    if failed == 0:        
        print ("\nYou won")
        break            
    guess = input("\nguess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print ("Wrong")  
        print ("You have", + turns, 'more guesses' )
        if turns == 0:           
            print ("You Lose"  )