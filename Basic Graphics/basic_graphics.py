from tkinter import *


def run():
    # On clicking, text appears on console
    print("Hey, you clicked me!!")

    # On clicking,text appears on screen
    new_text = Label(text="Hey, you clicked me!!", fg="red", bg="yellow")
    new_text.pack()


# Screen
screen = Tk()
screen.title("My First Graphics Program")
screen.geometry("500x500")

# Welcome Text
welcome_text = Label(text="Welcome to my first graphics program.", fg="green", bg="light blue")
welcome_text.pack()

# Button
click_me = Button(text="Click Me", fg="red", bg="light green", command=run)  # --> add (height=10, width=20) for more modification.
click_me.place(x=10, y=20)


screen.mainloop()
