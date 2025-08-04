import random

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ('<h1 style="font-family:Arial">Guess a number between 0 and 9:</h1>'
            '<img style="width:500px" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3k1YTIzeGp6cDhwdHU1dTcyd2d0amRidWZhbmdsa3h6ZnpremoxbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fDUOY00YvlhvtvJIVm/giphy.gif"/>')


answer = random.randint(0,9)

@app.route("/<user_guess>")
def detecter(user_guess):
    try:
        guess = int(user_guess)
    except ValueError:
        return '<h1 style="color:orange; font-family:Arial">Please enter a valid number between 0 and 9.</h1>'

    if guess > answer:
        return ('<h1 style="color:red; font-family:Arial">Too high, Try again!</h1>'
                '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzI0c20wcHo3ajJnNWdvYnJsMzk2em0ybDZpYXB4ZTE4eXZrNWpoMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qPuhFBQt8xLEY/giphy.gif" style="width:500px"/>')
    elif guess < answer:
        return ('<h1 style="color:purple; font-family:Arial">Too low, Try again!</h1>'
                '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmZ0eTB4NWhmZXlzY2FrZDkyenVmemNsdGJteTA0eHFkbXFpcWdvbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TzxfXbIIkWUQo/giphy.gif" style="width:500px"/>')
    else:
        return ('<h1 style="color:green; font-family:Arial">You found me !</h1>'
                '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZzdHBwdTVsMzNzdzhod3lzd2k0cDM0ejJuajN6OHVvcnp1MHJhNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oJWx7MtpR2qdi/giphy.gif" style="width:500px"/>')

if __name__ =="__main__":
    app.run(debug=True)