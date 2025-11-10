# def add(*args):
#     print(type(args))
#     sum_num = 0
#     for n in args:
#         sum_num += n
#     print(sum_num)
#
#
# def calculate(n, **kwargs):
#     print(type(kwargs))
#     n += kwargs.get("add")
#     n *= kwargs.get("multiply")
#     print(n)
#
#
# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# calculate(2, add=3, multiply=5)

from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
