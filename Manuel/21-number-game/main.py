def user(player):
    while True:
        try:
            choice = int(input(f"Player {player}, enter your choice (1, 2, or 3): "))
            if choice>=1 and choice<=3:
                return choice
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play():
    sum = 0
    current_player = 1

    print("Let's play 21 number game!")
    print("The player who reaches 21 first loses.")
    print("Each player can choose to count 1, 2, or 3 numbers in their turn.")

    while sum < 21:
        print(f"\nCurrent number: {sum}")
        choice = user(current_player)
        if (choice+sum)>=21:
            print(f"Player {current_player} loses!")
            break
        sum += choice
       
        current_player = 3 - current_player  

play()

