import random

computer = random.choice([1, 0, -1])
"""
1 for snake
-1 for water
0 for gun
"""
your_dict = {'s': 1, 'w': -1, 'g': 0}
reverse_dict = {1: 'snake', -1: 'water', 0: 'gun'}

you_choice = input("Enter your choice (s for snake, w for water, g for gun): ")

# Check if the user input is valid
if you_choice not in your_dict:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    you = your_dict[you_choice]

    print(f"You chose {reverse_dict[you]}")
    print(f"Computer chose {reverse_dict[computer]}")

    if computer == you:
        print("Game draw")
    elif (computer == 1 and you == -1) or \
         (computer == -1 and you == 0) or \
         (computer == 0 and you == 1):
        print("Computer wins, sorry")
    else:
        print("You win, wow")
