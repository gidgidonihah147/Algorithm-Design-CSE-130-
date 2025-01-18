# 1. Name: 
#    Tristin Parker
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    Quick review of python meant to test the students basic knowledge of Python and help review if needed
# 4. What was the hardest part? Be as specific as possible.
#    I havent coded in python for a little bit, I've been doing alot of web based coding for other classees. I had to look up some of the differences between them. Once I got going it came back quick though.
# 5. How long did it take for you to complete the assignment?
#    Roughly 0.4 Hours (Excluding setup of github for the course); 0.6 hours with github and folder setup.

import random

# Let the user know the Game introduction.
print("This is the 'guess a number' game.")
print("You try to guess a random number in the smallest number of attempts.")
print("\tIf you guess too high, you will get the prompt- Too high!")
print("\tIf you guess too low, you will get the prompt- Too low!")

# Let the user choose the high threshold so the game is not the same each time.
value_max = int(input("Pick a positive integer as the high threshold: "))

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Prompt the user to start the loop for the game
print(f"Guess a number between 1 and {value_max}.")

# Create the empty aray and create guess to allow the user to override the guess count.
guesses = []
guess = 0

# Play the guessing game. Only loop while we dont equal the number allowing to dump out after the correct guess.
while guess != value_random:
    # Prompt the user for a number.
    guess = int(input("> "))

    # Store the number in an array so it can be displayed later.
    guesses.append(guess)

    # Was the guess too high, too low, or just right.
    if guess > value_random:
        print("\tToo high!")
    elif guess < value_random:
        print("\tToo low!")

# Print the guesses made, and the total count of guesses made.
print(f"You were able to find the number in {len(guesses)} guesses.")
print("The numbers you guessed were:", guesses)