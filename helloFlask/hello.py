from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ('<h1 style="text-align:center; font-family:Arial">Hello, World!</h1>'
            '<p style="font-family:Arial">This is a paragraph.</p>'
            '<img style="height:500px" src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjY3cTExYTJ3ZWc0cm5vOHZsZ2kwcDNtdWR4bzBubnBtNWFzb2ZocyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4VglqgTazN7YQ/giphy.gif" />')


def make_bold(function):
    def wrapper():
        "<b>function()</b>"



@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "<h1>Bye ! </h1>"

# @app.route("/<name>/1")
# def greet(name):
#     return f"Hello there {name} !"

# @app.route("/username/<path:name>")
# def greet(name):
#     return f"Hello there {name} !"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old ! !"


print(random.__name__)
print(__name__)

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)



