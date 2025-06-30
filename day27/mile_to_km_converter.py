from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=km)

miles_input = Entry(width=10)
miles_label = Label(text="Miles")
is_equal_label = Label(text="is equal to")
km_result_label = Label(text=0)
km_label = Label(text="Km")
calculate_button = Button(text="Calculate", command=miles_to_km)

miles_input.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
km_result_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calculate_button.grid(column=1, row=2)

































window.mainloop()