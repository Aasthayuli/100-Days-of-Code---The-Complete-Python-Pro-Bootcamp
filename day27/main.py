from tkinter import *

window = Tk()
window.title("My First GUI Program.")
window.minsize(width=500, height=300)

# Label
# my_label = Label(text= "I am a Label.", font=("Arial",24, "bold"))
# my_label.pack() # places the label on the screen
#
# my_label = Label(text= "I am a Label2.", font=("Arial",24, "bold"))
# my_label.pack(side= "left")
#
# my_label = Label(text= "I am a Label2.", font=("Arial",24, "bold"))
# my_label.pack(side= "bottom")

# my_label = Label(text= "I am a Label2.", font=("Arial",24, "bold"))
# my_label.pack(expand= True)  # places from same width and height on the screen

# changing the text for label
# my_label["text"] = "New text"
# my_label.config(text = "New Text")
# my_label.place(x=0, y=0)



# Button
# def button_clicked():
#     print("I got clicked!")
#     # my_label.config(text="Button got clicked!")
#     new_text = textfield2.get() # textfield2.get() gets the value from the textfield
#     my_label.config(text=new_text)

# button = Button(text="Click me", command=button_clicked)
# button.pack()
#
# # Entry component
# textfield = Entry()
# textfield.pack()
#
# textfield2 = Entry(width=50)
# textfield2.pack()



new_label = Label(text="New text")
new_label.grid(column =0, row =0)

def button_clicked():
    new_label.config(text="new text2")

button = Button(text="clickme2", command=button_clicked)
button.grid(column=1, row=1)

textfield3 = Entry(width=10)
print(textfield3.get())
textfield3.grid(column = 2, row = 2)














# import turtle
# tim = turtle.Turtle()

# arguments with default values
# tim.write("some text", font= ("Times New Roman", 20, "bold"))














window.mainloop()  # should always be at the end of the program