from tkinter import *


# Defining command functionality
def save_info():
    print("CLICKED!!")  # --> Printing on the console
    first_name = first_name_var.get()
    last_name = last_name_var.get()
    age = age_var.get()
    age = str(age)
    print(f"First Name: {first_name}\nLast Name: {last_name}\nAge: {age}")  # --> Checking functionality

    # Writing the file
    f_hand = open("user.txt", "w")
    f_hand.write(f"First Name: {first_name}\n")
    f_hand.write(f"Last Name: {last_name}\n")
    f_hand.write(f"Age: {age}\n")
    f_hand.close()

    print(f"User {first_name} has been registered successfully!")  # --> Prints on the console

    # Clearing the form/screen
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    age_entry.delete(0, END)


# Initializing screen display
screen = Tk()
screen.geometry("500x500")
screen.title("Python Form")
heading = Label(text="Basic Python Registration Form", bg="grey")
heading.pack()

# User Labels
first_name_label = Label(text="First Name:")
last_name_label = Label(text="Last Name:")
age_label = Label(text="Age:")

# Placing the user labels
first_name_label.place(x=15, y=70)
last_name_label.place(x=15, y=140)
age_label.place(x=15, y=210)

# Storing the variables
first_name_var = StringVar()
last_name_var = StringVar()
age_var = IntVar()

# Creating Entries
first_name_entry = Entry(textvariable=first_name_var, width=30)
last_name_entry = Entry(textvariable=last_name_var, width=30)
age_entry = Entry(textvariable=age_var, width=15)

# Positioning the Entries
first_name_entry.place(x=15, y=100)
last_name_entry.place(x=15, y=170)
age_entry.place(x=15, y=240)

# Creating register button
register_btn = Button(text="REGISTER", width=20, height=1, bg="light blue", command=save_info)
register_btn.place(x=15, y=310)

screen.mainloop()
