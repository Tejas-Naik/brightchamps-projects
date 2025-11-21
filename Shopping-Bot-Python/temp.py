print("Welcome to the Adventure Story!")
name = input("What is your name? ")
print(f"Hello, {name}! Let's begin the adventure.")

print("\nOnce upon a time, you find yourself in a dark forest.")
print("You have three paths ahead of you: left, right, and straight.")
    
choice1 = input("Which path do you choose? (left/right/straight): ")

if choice1 == "left":
        print("You come across a river. You can swim across or look for a bridge.")
        choice2 = input("What do you do? (swim/look for a bridge): ")

        if choice2 == "swim":
            print("You swim across the river but encounter a dangerous creature.")
            print("Sadly, you didn't make it. Game over!")
        elif choice2 == "look for a bridge":
            print("You find a hidden bridge and cross the river safely.")
            print("On the other side, you discover a treasure chest full of gold!")
            print("Congratulations! You win!")
        else:
            print("Invalid input. Game over!")

elif choice1 == "right":
        print("You encounter a group of bandits!")
        choice3 = input("Do you try to fight them or run away? (fight/run): ")

        if choice3 == "fight":
            print("You fought bravely, but the bandits were too strong.")
            print("Unfortunately, you didn't make it. Game over!")
        elif choice3 == "run":
            print("You managed to escape and find a village nearby.")
            print("The villagers are friendly and offer you shelter.")
            print("Congratulations! You are safe now.")
            print("You survived and the adventure ends here.")
        else:
            print("Invalid input. Game over!")

elif choice1 == "straight":
        print("You come across a cave entrance.")
        print("You can either enter the cave or go back to choose another path.")
        
        choice4 = input("What do you do? (enter/go back): ")

        if choice4 == "enter":
            print("You bravely enter the cave and find a hidden treasure!")
            print("Congratulations! You win!")
        elif choice4 == "go back":
            print("You decide not to risk it and go back to the forest.")
            print("After some time, you find your way out of the forest.")
            print("The adventure ends here.")
        else:
            print("Invalid input. Game over!")

else:
        print("Invalid input. Game over!")