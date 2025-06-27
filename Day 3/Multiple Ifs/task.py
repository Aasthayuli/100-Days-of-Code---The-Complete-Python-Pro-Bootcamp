print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill=5
        print("Child tickets are $5.")
    elif age <= 18:
        bill=7
        print("Youth tickets are $7.")
    else:
        bill=12
        print("Adult tickets are $12.")


    wants_photo=input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == 'y':
        # Add $3 to the bill
        bill+=3
        print(f"your final bill is ${bill}.")
    elif wants_photo == 'n':
        print(f"Okay ! your final bill is ${bill}.")
    else:
        print("Enter either 'y' or 'n' only.")

else:
    print("Sorry you have to grow taller before you can ride.")
