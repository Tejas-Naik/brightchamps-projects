import random

print("Welcome to word jumble game!")
name = input("Enter the player name-> ")
word_list = ['butterfly', 'guitar', 'football', 'chocolate', 'rainbow', 'castle', 'unicorn', 'pizza', 'popcorn', 'ocean', 'elephant', 'bicycle', 'icecream', 'adventure', 'dinosaur', 'pencil', 'monkey', 'robot', 'baseball', 'cupcake']

quit_game = False

# GAME LOOP
while not quit_game:
    word = random.choice(word_list)
    jumbled_word = ""
    n = len(word)

    used_indices = []
    while len(used_indices) < n:
        index = random.randint(0, n - 1)
        if index not in used_indices:
            jumbled_word += word[index]
            used_indices.append(index)

    print("Here's the word you need to guess --> ", jumbled_word.lower())
    chances = 5

    while chances > 0:
        guess = input("\nEnter your guess--> ")
        if guess.lower() == word.lower():
            print(f"Yay!! Congratulations {name.capitalize()}. You guessed it right.")
            break
        chances -= 1
        print("Chances left:", chances)

    else:
        print("Oops! You lost all your chances. The word is", word)
        print("Game over")

    print("\nDo you want to continue the game? (y/n)")
    q = input("Press n to quit and y to continue ")
    if q.lower() == 'n':
        quit_game = True

