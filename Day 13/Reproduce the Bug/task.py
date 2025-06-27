from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # randint(a,b) generates any number from a to b including a and b.
dice_num = randint(0, 5)
print(dice_images[dice_num])
