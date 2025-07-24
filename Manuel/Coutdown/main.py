import random
import time
print('👧')
print("Hello students, lets play a guessing game ")
time.sleep(2)
print("Hint- Something you eat")
fruits = ['apple','banana','grapes','guava','pineapple']
fruit = random.choice(fruits)
name = input("Please enter the player's name ? ")
guessedLetters = ''
chance = 10 
print("Okay ! Let's start guessing. ")
while chance > 0:
    guess = input("Guess the word: ")
    guessedLetters += guess
    wrong = 0
    for letter in fruit:
        if letter in guessedLetters:
            print(letter)
        else:
            print("_")
            wrong = 1
    if wrong == 0:
        print("Congratulations! ",name,"You guessed all the letters correct.")
        print("The word is: ",fruit)
        break
    if guess not in fruit:
        chance -= 1
        print("Wrong guess. This letter is not in word.")
        print("You have", chance , 'more guess chances. ') 
        print("Hint-It's a fruit ")
        if chance == 0:
            print("Sorry! Your number of chances are over. You loose.")
