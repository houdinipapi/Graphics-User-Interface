from tkinter import *


def run():
    # On clicking, text appears on console
    print("Hey, you clicked me!!")

    # On clicking,text appears on screen
    new_text = Label(text="Hey, you clicked me!!", fg="red", bg="yellow")
    new_text.pack()


def name_btn():
    new_name = name_storage.get()
    print(new_name)


def delete_btn():
    new_name.delete(0, END)


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

name_button = Button(text="Name", fg="light blue", bg="green", command=name_btn)
name_button.place(x=200, y=40)

delete_button = Button(text="Delete", fg="red", bg="yellow", command=delete_btn)
delete_button.place(x=200, y=80)

# Entry type
name_storage = StringVar()
new_name = Entry(textvariable=name_storage)
new_name.pack()


screen.mainloop()
