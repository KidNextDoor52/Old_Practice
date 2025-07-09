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
canvas.pack()

window.mainloop()