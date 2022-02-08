import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

option = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if -1 < option < 3:
    print("You chose\n")
    print(options[option])

    com_option = random.randint(0, 2)

    print("Computer chose:\n")
    print(options[com_option])

    adjusted_option = (option + 1) % 3
    adjusted_com_option = (com_option + 1) % 3

    if option == com_option:
        print("Draw!")
    elif adjusted_option == com_option:
        print("Computer wins!")
    elif option == adjusted_com_option:
        print("You win!")

else:
    print("Invalid option, you lose.")