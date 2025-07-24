
# This is used to choose a word among the list. 
import random

words = ['bright','champs','coding','python','student']
 
word = random.choice(words) # Here we are using the choice() function
                            # among random module to choose a word from words 
 
name = input("Please enter the player's name ? ")

guessedLetters = '' # We are defining the variable here with string. 
 
# any number of chance can be used here
chance = 10
 
print("Okay ! Let's start guessing. ")
while chance > 0:
    
    # This will start taking the letters for checking. 
    guess = input("Guess a letter of the word: ")
     
    # in guessedLetters we will keep all the letter which we have inserted. 
    guessedLetters += guess

    # checks if the user is all wrong or correct. 
    wrong = 0
     
    # in word all the letters will be checked one by one using loop
    for letter in word:
        # if letter which user has inserted is in it then print it. 
        if letter in guessedLetters:
            print(letter)
        
        else:
            print("_")
            wrong = 1
             
    # if wrong is zero then it means all the words matched. 
    if wrong == 0:

        print("Congratulations! ",name,"You guessed all the letters correct.")
         
        print("The word is: ", word)
        break
     
    # if the letter which we guessed is not in word 
    if guess not in word:
         
        chance -= 1 # no of chances will be decreased by 1
         
        print("Wrong guess. This letter is not in word.")
         
        # We explained more chances user can try. 
        print("You have", chance , 'more guess chances. ')
         
        # If chances are zero we'll print you loose. 
        if chance == 0:
            print("Sorry! Your number of chances are over. You loose.")