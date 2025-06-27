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
import random


game_images=[rock, paper, scissors]

user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if(0<=user_input<=2):
    print(game_images[user_input])
comp_choice=random.randint(0,2)
print("Computer chose:")
print(game_images[comp_choice])


print("Computer chose: "+ str(comp_choice))
if user_input >=3 or user_input <0:
    print("You typed an invalid number. You Lose!")
elif user_input == 0 and comp_choice == 2:
    print("You Win!")
elif user_input == 2 and comp_choice == 0:
    print("You Lose!")
elif comp_choice > user_input:
    print("You lose!")
elif comp_choice < user_input:
    print("You win!")
elif  user_input == comp_choice:
    print("It's a Draw!")

