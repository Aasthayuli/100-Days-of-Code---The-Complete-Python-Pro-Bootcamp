import random

from art import logo, vs
from game_data import data

print(logo)

current_score = 0
option2 = random.choice(data)

def game():

    global option2
    option1 = option2
    option2 = random.choice(data)

    print(f"Compare A: {option1['name']}, a {option1['description']}, from {option1['country']}.")
    print(vs)
    print(f"Against B: {option2['name']}, a {option2['description']}, from {option2['country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_choice == 'A':
        user_answer = option1['name']
    else:
        user_answer = option2['name']

    if option2['follower_count'] > option1['follower_count']:
        answer = option2['name']
    else:
        answer = option1['name']

    global current_score
    if user_answer == answer:
        current_score += 1
        print("\n" * 20)
        print(logo)
        print(f"You're right! Current Score: {current_score}.")
        game()
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}.")


game()

