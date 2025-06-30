from tkinter import *

window = Tk()
window.title("Grid placing")
window.minsize(width=500, height=300)
window.config(padx= 100, pady= 100)

text_label = Label(text="label")
text_label.grid(column= 0, row= 0)
# text_label.config(padx=50, pady=50)

def clickme():
    text_label.config(text="label is changed.")

btn = Button(text="button", command=clickme)
btn.grid(column=2, row=2)

new_btn = Button(text="button2")
new_btn.grid(column=3, row=1)

entry = Entry(width=10)
entry.grid(column=4,row=4)



























window.mainloop()