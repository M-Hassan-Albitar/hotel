from tkinter import *
from tkinter import messagebox


# ====================================== DATA UI ======================================================== #
def clicked():
    dt_window = Tk()
    dt_window.minsize(width=600, height=400)
    dt_window.title("Data")
    part_label = Label(dt_window, text="Flat NO :")
    part_label.grid(row=0, column=0)
    name_label = Label(dt_window, text="Name :")
    name_label.grid(row=1, column=0)
    phone_label = Label(dt_window, text="Phone :")
    phone_label.grid(row=2, column=0)
    cash_label = Label(dt_window, text="Cash :")
    cash_label.grid(row=3, column=0)
    std_label = Label(dt_window, text="Start Date :")
    std_label.grid(row=4, column=0)
    exd_label = Label(dt_window, text="Exp Date :")
    exd_label.grid(row=5, column=0)
    flat = Entry(dt_window)
    flat.grid(row=0, column=1)
    name = Entry(dt_window)
    name.grid(row=1, column=1)
    phone = Entry(dt_window)
    phone.grid(row=2, column=1)
    cash = Entry(dt_window)
    cash.grid(row=3, column=1)
    std = Entry(dt_window)
    std.grid(row=4, column=1)
    exd = Entry(dt_window)
    exd.grid(row=5, column=1)
    new_save = Button(dt_window, text="Save")
    new_save.grid(row=6, column=0)


# ====================================== MAIN UI ====================================================== #
main_window = Tk()
main_window.geometry("250x300")
main_window.title("Hotel")
canvas = Canvas()
img = PhotoImage(file="img2.png", width=163, height=122)
canvas.create_image(80, 60, image=img)
canvas.grid(row=0, column=1)

# Buttons
btn = Button(text="New", background="black", foreground="white", command=clicked)
btn.grid(row=1, column=0)
main_window.mainloop()
