import random

print("Welcome to the Number Guessing game!")
print("I am thinking of the number between 1 and 100.")

num = random.randint(1,100)
difficulty = input("Choose a difficulty.Type 'easy' or 'hard': ")

def game():
    i = 10
    user = -1
    flag = True
    if difficulty == "hard":
        i = 5
        print("You have 5 attempts remaining to guess the number.")

    if difficulty == "easy":
        i = 10
        print("You have 10 attempts remaining to guess the number.")

    while flag:
        user = int(input("Make a guess: "))
        if user > num:
            print("Too high.\nGuess again.")
            i-=1
            print(f"You have {i} attempts remaining to guess the number.")
            if i == 0:
                print(f"You Lose. The answer was {num}.")
                flag =False
        if user < num:
            print("Too low.\nGuess again.")
            i-=1
            print(f"You have {i} attempts remaining to guess the number.")
            if i == 0:
                print(f"You Lose. The answer was {num}.")
                flag =False
        if user == num :
            print(f"You got the answer the right. The answer was {num}.")
            flag = False




game()
