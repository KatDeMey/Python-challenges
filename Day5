# Rock Paper Scissors challenge

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n "))
computer_choice = random.randint(0, 2)

#Check valid inputs
if 0 <= user_choice <= 2:
    invalid_number = False
    print(hands[user_choice])
else:
    invalid_number = True

print(f"Computer chose:\n{hands[computer_choice]}")

if user_choice == computer_choice:
    print("It's a tie!")
elif ((computer_choice == 0 and user_choice == 1) or (computer_choice == 1 and user_choice == 2)
      or (computer_choice == 2 and user_choice == 0)):
    print("You Win!")
else:
     if invalid_number:
         print("You chose an invalid number. You lose!")
     else:
        print("You Lose!")
