print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

boat = r'''
     _
    /|\
   /_|_\
 ____|____
 \_o_o_o_/
~~~~~~~~~~~~~~~~~
'''

continue_adventure = True
direction = input("You follow a path and have reached a crossroads. "
                  "Which way to you go? Left (L) or Right (R)?\n ").lower()
moat_action = ("You went left until you came across a castle with a giant moat. "
               "Do you A) Swim or B) Wait. Type A or B:\n ")
door = ("You find 3 doors to enter the castle. "
        "Do you go through the A) Red, B) Yellow, or C) Blue door? ")

# # Direction
if not (direction == "left" or direction == "l"):
    continue_adventure = False
    print("You went right... into a bear trap and got eaten by a wild animal.\nGame Over.")
else:
    # Moat:
    moat_action = input(moat_action).lower()
    if not (moat_action == "wait" or moat_action == 'b'):
        print(" You were attacked by a trout. Game over")
    else:
        print(" Yay a ferry came to take you across!")
        #doors
        door = input(door).lower()
        if door == "a":
            print("Burned by fire. Game Over")
        elif door == "b":
            print("you win!")
        elif door == "c":
            print("Eaten by beasts. Game Over")
        else:
            print("Instructions unclear. Game over")


# # Direction
# if not (direction == "left" or direction == "l"):
#     continue_adventure = False
#     print("You went right... into a bear trap and got eaten by a wild animal.\nGame Over.")
# else:
#     moat_action = input(moat_action).lower()
#
# # Moat Time
# if continue_adventure:
#     if not (moat_action == "wait" or moat_action == 'b'):
#         continue_adventure = False
#         print(" You were attacked by a trout. Game over")
#     else:
#         print(boat)
#         print(" Yay a ferry came to take you across!")
#         door = input(door).lower()
#
# # Door Time
# if continue_adventure:
#     if door == "a":
#         continue_adventure = False
#         print("It's a room full of fire. Game Over")
#     elif door == "b":
#         print("You found the treasure. You win!")
#     elif door == "c":
#         continue_adventure = False
#         print("You enter a room full of beasts. Game Over")
#     else:
#         print("Instructions unclear. Game over")
