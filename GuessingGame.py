# This is a guess the number game. #First line is a comment.
import random # Second line is an important statement. Statements are instructions that perform some action but don't evaluate expressions.

GuessesTaken = 0 # Line 4 creates a new variable named GuessesTaken. You'll store the number of guesses a player makes within this variable.

print('Hello! What is your name?')
myName = input() # Line 6 is a function to call to the print() function.

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while GuessesTaken < 6 
    print('Take a guess.') # There are four spaces in front of print..
    guess = input()
    guess = int(guess)
    
    GuessesTaken = GuessesTaken + 1
    
    if guess < number: 
        print('Your guess is too low') # There are eight spaces in front of print
        
    if guess > number:
        print ('Your guess is too high')
        
    if guess == number:
        break
        
if guess == number:
    GuessesTaken = str(GuessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + GuessesTaken + ' guesses!')
    
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
