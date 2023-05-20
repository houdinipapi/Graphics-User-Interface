from tkinter import *

# Initializing screen display
screen = Tk()
screen.geometry("500x500")
screen.title("Python Form")
heading = Label(text="Basic Python Form", bg="grey")
heading.pack()

# User Labels
first_name_label = Label(text="First Name:")
last_name_label = Label(text="Last Name:")
age_label = Label(text="Age:")

# Placing the user labels
first_name_label.place(x=15, y=70)
last_name_label.place(x=15, y=140)
age_label.place(x=15, y=210)

screen.mainloop()
