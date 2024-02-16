# CowsAndBulls.py
# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user 
# guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in 
# the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes 
# throughout teh game and tell the user at the end.

import random

random_or_set = input("Enter a number from 2-10, or type the word random to have a randomly generated word length:   ")

if random_or_set == 'random':
    print("You've selected a random length.")
    length = random.randint(2,10)
else:
    length = int(random_or_set)

answer = random.sample("0123456789",length)
answer_text = "".join(answer)

show_answer = input("Do you want to see the answer so you can test out how the game works? y/n:   ")
if show_answer == 'y':
    print("The answer that you are supposed to end up with is " + str(answer_text) + ".")


# set the initial guess to 0 so that it won't stop before it even starts
guess = 0
c = 0

# print(answer_text)



# until the user gets the right number, or the user enters exit it will keep asking them to guess a number
while guess != answer_text and guess != "exit":

    cows = 0
    bulls = 0

# don't convert the user input yet because it could be a string at some point
    if c == 0:
        guess = input("Guess a number that is "+ str(length) + " digits long:   ")
    else:
        guess = input("Guess again:   ")

# if the user inputs exit that it stops
    if guess == "exit":
        break

# since the program did not stop, assume the user input a number
    guess = str(guess)

    if guess == answer_text:
        c+= 1
        if c == 1:
            print("You've guessed the number in",str(c),"guess!")
        else:
            print("You've guessed the number in",str(c),"guesses!")
        break
    else:
        for i in guess:
            if i in answer:
                if guess.index(i) == answer.index(i):
                    cows += 1
                    continue
                else:
                    bulls += 1
                    continue
    print(str(cows)," cows and ",str(bulls),"bulls.")
    c += 1
    

        