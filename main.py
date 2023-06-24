import json
from tkinter import *
from tkinter import messagebox
import webbrowser

BG = "#070A52"
BTN = "#D21312"
UPDATE = "#F15A59"
T = "white"
CLEAR = "green"


# ====================================== LOGIC ======================================================== #
def save():
    f_num = flat.get()
    f_name = name.get()
    f_phone = phone.get()
    f_cash = cash.get()
    f_std = std.get()
    f_exd = exd.get()

    new_data = {
        f_num: {
            "name": f_name,
            "phone": f_phone,
            "cash": f_cash,
            "std": f_std,
            "exd": f_exd,
        }
    }

    if len(f_num) == 0 or len(f_phone) == 0 or len(f_cash) == 0 or len(f_std) == 0 or len(f_exd) == 0:
        messagebox.showwarning("Error", "Fields must be not empty.")
    else:
        try:
            with open(file="data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            if f_num not in data:
                data.update(new_data)
                with open(file="data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            else:
                messagebox.showinfo("Info", "Exist before.")
        finally:
            flat.delete(0, END)
            name.delete(0, END)
            phone.delete(0, END)
            cash.delete(0, END)
            std.delete(0, END)
            exd.delete(0, END)


def search_data():
    s_num = search.get()
    if len(s_num) > 0:
        try:
            with open(file="data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo("Error", "No Data File.")
        else:
            if s_num in data:
                name.insert(0, data[s_num]["name"])
                phone.insert(0, data[s_num]["phone"])
                cash.insert(0, data[s_num]["cash"])
                exd.insert(0, data[s_num]["exd"])
                # print(data[s_num])
                with open(file="report.txt", mode="w") as report_file:
                    d_num = s_num
                    d_name = data[s_num]["name"]
                    d_phone = data[s_num]["phone"]
                    d_cash = data[s_num]["cash"]
                    d_std = data[s_num]["std"]
                    d_exd = data[s_num]["exd"]
                    report_file.write(
                        f"===================\nNumber: {d_num}\n===================\nName: {d_name}\n===================\nPhone: {d_phone}\n===================\nCash: {d_cash}\n===================\nStart: {d_std}\n===================\nEnd: {d_exd}\n===================\n")
                webbrowser.open("report.txt")
            else:
                messagebox.showinfo("No Data", "No Data.")
                # std.insert(END, data[s_num]["std"])
    else:
        messagebox.showinfo("Error", "Search field can not be empty.")


def update():
    f_name = name.get()
    f_phone = phone.get()
    f_cash = cash.get()
    f_exd = exd.get()
    u_search = search.get()
    if len(u_search) > 0:
        with open(file="data.json", mode="r") as data_file:
            data = json.load(data_file)
        if u_search in data:
            #     # print(data[u_search])
            data[u_search]["name"] = f_name
            data[u_search]["phone"] = f_phone
            data[u_search]["cash"] = f_cash
            data[u_search]["exd"] = f_exd
        with open(file="data.json", mode="w") as data_file:
            json.dump(data, data_file, indent=4)

        name.delete(0, END)
        phone.delete(0, END)
        cash.delete(0, END)
        exd.delete(0, END)
    else:
        messagebox.showinfo("Error", "Search field can not be empty.")


def clear_all():
    flat.delete(0, END)
    name.delete(0, END)
    phone.delete(0, END)
    cash.delete(0, END)
    std.delete(0, END)
    exd.delete(0, END)
    search.delete(0, END)


# ====================================== MAIN UI ====================================================== #

# Main Window
window = Tk()
window.minsize(width=650, height=350)
window.resizable(False, False)
window.title("Hotel")
window.config(padx=10, pady=20, background=BG)

# Labels
part_label = Label(text="Flat NO :", padx=10, pady=10, background=BG, foreground=T, font=("Arial", 14))
part_label.grid(row=2, column=0)
name_label = Label(text="Name :", padx=10, pady=10, background=BG, foreground=T, font=("Arial", 14))
name_label.grid(row=3, column=0)
phone_label = Label(text="Phone :", padx=10, pady=10, background=BG, foreground=T, font=("Arial", 14))
phone_label.grid(row=4, column=0)
cash_label = Label(text="Cash :", padx=10, pady=10, background=BG, foreground=T, font=("Arial", 14))
cash_label.grid(row=5, column=0)
std_label = Label(text="Start Date :", padx=10, pady=10, background=BG, foreground=T, font=("Arial", 14))
std_label.grid(row=6, column=0)
exd_label = Label(text="Exp Date :", padx=10, pady=10, background=BG, foreground=T, font=("Arial", 14))
exd_label.grid(row=7, column=0)
search_label = Label(text="Search :", padx=10, pady=10, background=BG, foreground=T, font=("Arial", 14))
search_label.grid(row=2, column=2)

# Entries
flat = Entry(font=("Arial", 14))
flat.grid(row=2, column=1)
name = Entry(font=("Arial", 14))
name.grid(row=3, column=1)
phone = Entry(font=("Arial", 14))
phone.grid(row=4, column=1)
cash = Entry(font=("Arial", 14))
cash.grid(row=5, column=1)
std = Entry(font=("Arial", 14))
std.grid(row=6, column=1)
exd = Entry(font=("Arial", 14))
exd.grid(row=7, column=1)
search = Entry(font=("Arial", 14))
search.grid(row=2, column=3)

# Buttons
new_save = Button(text="Save", width=37, background=BTN, highlightthickness=0, foreground=T, pady=7, command=save)
new_save.grid(row=8, column=0, columnspan=2)
new_search = Button(text="Search", width=23, background=BTN, highlightthickness=0, foreground=T, pady=7,
                    command=search_data)
new_search.grid(row=3, column=3, columnspan=2)
new_update = Button(text="Update", width=23, background=UPDATE, highlightthickness=0, foreground=T, pady=7,
                    command=update)
new_update.grid(row=4, column=3, columnspan=2)
new_update = Button(text="Clear", width=23, background=CLEAR, highlightthickness=0, foreground=T, pady=7,
                    command=clear_all)
new_update.grid(row=8, column=3, columnspan=2)

window.mainloop()
