from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)


    password = " ".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }

    }

    if len(website) == 0 or len(password) == 0:
         messagebox.showinfo(title="Oops" , message="Please make sure you haven't left any fields empty. ")
    else:
        try:  #TRY BLOCK CAN FAIL
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:  #DEALS WITH ANY FAILURES THAT OCCUR
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:   #HAS THE CODE THAT NEEDS TO RUN IF NO ISSUES
            #updating old data (dictionary) with the new data 
            # NEW DATA IS A DICTIONARY     DATA FILE IS THE FILE OPENED IN JSON FORM
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                #saving the updated data
                json.dump(data, data_file, indent=40)

        finally: #DOESN'T MATTER IF THERE WAS OR WASN'T AN ISSUE WILL RUN
            #CLEARS OUR WEBSITE PASSWORDS AND ENTRY
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#----------------------------Find Password---------------------------------
                
def find_password():
    website = website_entry.get()
    try:#if the file isn't found
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:#what to do if the data is not found | Exceptions should be used when there isn't an easy if/else
            messagebox.showinfo(title="Erro" , message="No Data File Found. ")
    else: #if it was successful finding the file
        if website in data:
            #data is the whole dictionary, email and password are nested dictionaries
            email = data[website]["email"] #using the key "email" to access the value
            password = data[website]["password"] # using the key "password" to access the value
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:#this shows the error if there is something not found that we search
            messagebox.showinfo(title="Error", message=f"No details for {website} exists .")



          
# ---------------------------- UI SETUP ------------------------------- #
"""
here we are learning about the GUI
#  window = Tk() starts the window and you type your whole GUI within that

#  window.mainloop() is what closes the window 
make sure to have this at the end of your desired GUI
"""
# ------------------------- File Handling ------------------------
#file_path = os.path.abspath("C:\\Users\\mccra\\OneDrive\\Documents\\GitHub\\Old_Practice\\day 29")
#file = os.path.join(file_path, "data.txt") 

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="day-29/logo.png")
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
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "robert@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()