# Dice game:
#
# Let's make a game that rolls a dice and picks a winner. You or the CPU!
#
# Start the game with a welcome message and ask if the user is ready to play.
# Store the number in a variable
# Use the random library and a method from that library to roll a number 1-6

import random

print("Welcome to the Dice Game!")
player_name = input("Enter your name: ")
ready = input("Are you ready to play? (yes/no): ")

if ready == "yes":
    # player_name = input("Enter your name: ")
    print(f"Hi {player_name.upper()}! Welcome to the game!")
else:
    print("May be next time!")
    exit()

# Get the user's name and start a loop (While loop recommended)

ready = True

while ready:
    player_dice_roll = random.randint(1, 6)
    print(f"{player_name} rolled a {player_dice_roll}.")

# Do the same for the computer

    cpu_dice_roll = random.randint(1, 6)
    print(f"CPU rolled a {cpu_dice_roll}.")

# Compare the two numbers, whose was bigger? Tell the user (if it was a tie, what then?) and end the game
    if player_dice_roll > cpu_dice_roll:
        print(f"Congratulations, {player_name.upper()}! You win!")
    elif player_dice_roll < cpu_dice_roll:
        print(f"Sorry, {player_name.upper()}! CPU wins!")
    else:
        print("It's a tie!")

# Start the game with a welcome message and ask if the user is ready to play.
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
print("Thank you for playing the Dice Game!")





