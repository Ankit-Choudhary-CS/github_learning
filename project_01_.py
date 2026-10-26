'''
Project 01 - Python Basics
1 for snake 
-1 for water 
0 for gun



'''
import random

# Computer's choice: randomly select from 1 (snake), -1 (water), 0 (gun)
computer = random.choice([1, -1, 0])

# User input
youstr = input("Enter 's' for snake, 'w' for water, 'g' for gun: ")

# Map user input to corresponding number
youDict = {"s": 1, "w": -1, "g": 0}

# Check if the input is valid
if youstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    print(f"You chose{dict[you]}\n Computer chose{dict[computer]}")

    # Display choices
    print(f"Computer chose: {computer}")
    print(f"You chose: {you}")

    # Game logic
    if computer == you:
        print("It's a Draw!")
    else:
        if (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
            print("You win!")
        elif (computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer == 0 and you == 1):
            print("You lose!")
        else:
            print("Something went wrong!")
# The code above implements a simple game where the user can choose between snake,
# water, or gun and the computer randomly selects one of the three options. 
# the game then determines the winner based on the rules of the game. 

