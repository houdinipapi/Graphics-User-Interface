from tkinter import *


# Defining Error
def error():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("150x90")
    screen1.title("WARNING!!")
    Label(screen1, text="All fields are required!!", fg="red").pack()
    Button(screen1, text="OK", command=delete_error).pack()


# Defining delete functionality
def delete_error():
    screen1.destroy()


def delete_success():
    screen2.destroy()


# Defining success functionality
def success():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("150x90")
    screen2.title("SUCCESS!!")
    Label(screen2, text="Registration Successful!!", fg="green").pack()
    Button(screen2, text="OK", command=delete_success).pack()


# Registering a user
def register():
    username_text = username_var.get()
    password_text = password_var.get()

    if username_text == "" or password_text == "":
        error()
    else:
        success()


# Exiting main screen
def exit_screen():
    screen.destroy()


# Screen initialization
screen = Tk()
screen.geometry("500x500")
screen.title("Form Validation")

# Heading
heading = Label(text="Python Form Validation", fg="black", bg="grey", width=500, height=2)
heading.pack()

# Entry Labels
username_label = Label(text="Username:")
username_label.place(x=15, y=50)
password_label = Label(text="Password:")
password_label.place(x=15, y=120)

# Variables Storage
username_var = StringVar()
password_var = StringVar()

# Entries
username_entry = Entry(screen, textvariable=username_var, width=30)
username_entry.place(x=15, y=80)

password_entry = Entry(screen, textvariable=password_var, width=30, show="*")
password_entry.place(x=15, y=150)

# Validation Button
register_btn = Button(screen, text="REGISTER", width=10, fg="black", bg="light green", command=register)
register_btn.place(x=15, y=210)

# Exit Button
exit_btn = Button(screen, text="EXIT", width=7, fg="green", bg="light grey", command=exit_screen)
exit_btn.place(x=120, y=210)

screen.mainloop()
