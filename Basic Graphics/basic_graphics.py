from tkinter import *

# Screen
screen = Tk()
screen.title("My First Graphics Program")
screen.geometry("500x500")

# Welcome Text
welcome_text = Label(text="Welcome to my first graphics program.", fg="green", bg="light blue")
welcome_text.pack()

screen.mainloop()
