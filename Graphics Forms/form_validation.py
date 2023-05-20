from tkinter import *

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

screen.mainloop()
