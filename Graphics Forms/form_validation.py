from tkinter import *


def register():
    username_text = username_var.get()
    password_text = password_var.get()


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

screen.mainloop()
