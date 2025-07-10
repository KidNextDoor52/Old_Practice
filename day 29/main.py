from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
"""
here we are learning about the GUI
#  window = Tk() starts the window and you type your whole GUI within that

#  window.mainloop() is what closes the window 
make sure to have this at the end of your desired GUI
"""
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="day 29/logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Radiobutton(text="Add")
add_button.grid

window.mainloop()