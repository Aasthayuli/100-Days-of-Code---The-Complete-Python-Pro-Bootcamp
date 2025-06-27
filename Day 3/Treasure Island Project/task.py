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
quote='"'
left_or_right=input('You\'re at a cross road. Where do you want to go?Type "left" or "right"').lower()
if left_or_right== "left":
    swim_or_wait=input('You\'ve come to lake.\n'
                       'There is an island in the middle of the lake.\n'
                       'Type "wait" to wait for a boat.\n'
                       'Type "swim" to swim across.').lower()

    if swim_or_wait == 'wait':
        door=input("You arrive at the island unharmed.\n"
                   "There is a house with 3 doors. \n"
                   "One red, One yellow and One blue. \n"
                   "Which colour do you choose?").lower()
        if door == 'yellow':
            print(" You found the Treasure. You Win!")
        elif door == 'red':
            print("It's a room full of fire. Game Over.")
        elif door == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

