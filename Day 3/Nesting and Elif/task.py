print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("Enter your age: "))
    if age<=12 and age>0:
        print("Please pay $5.")
    elif age>12 and age<18:
        print("Please pay $7.")
    elif age>=18:
        print("Please pay $12.")
    else:
        print("Invalid Age !!")
else:
    print("Sorry you have to grow taller before you can ride.")
