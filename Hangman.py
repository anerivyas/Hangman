import time
import random

print "Hey there! Let's play Hangman. Good luck :)"

playerName = raw_input("What's your name?")

print "Hello, " + playerName, "time to play hangman!"


time.sleep(1)

print "Start guessing..."
time.sleep(0.5)


wordList = ["hello", "world", "apple", "rainbow", "mountain"]

word = (random.choice(wordList))

playersGuesses = ''

turns = 10


while turns > 0:         

    wrongGuess = 0             

    for letterGuessed in word:      

        if letterGuessed in playersGuesses:    
    
            print letterGuessed,    

        else:
    
            print "_",     
       
            wrongGuess += 1    

    if wrongGuess == 0:        
        print "You won"  


        break              

    print

    guess = raw_input("Guess a letter:") 

    playersGuesses += guess             



    if guess not in word:  
 
        turns -= 1        
 
        print "Wrong guess, try again"    

        
 
        print "You have", + turns, 'more guesses' 
 
        if turns == 0:           
    
            print "Sorry you lost the game. The word was " + word