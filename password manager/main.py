from tkinter import *
from tkinter import messagebox
import pandas
import random
import pyperclip
import json

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
big_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
small_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
           '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']


def generate_password():
    global big_letter, small_letter, num, symbols
    password = ''
    password_entry.delete(0, END)
    for a in range(1, 4):
        password = password + (big_letter[random.randint(0, 2)])
        password = password + (small_letter[random.randint(0, 25)])
        password = password + (num[random.randint(0, 9)])
        password = password + (symbols[random.randint(0, 25)])
    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please make sure you have not left any field blank')
    else:
        final = messagebox.askokcancel(title='Website', message=f'These are the details entered: \nEmail : {email}'
                                                                f'\nPassword : {password} \nIs it ok to save?')
        if final:
            data_dictionary = {
                'Website': [website],
                'email': [email],
                'password': [password]
            }
            data = pandas.DataFrame(data_dictionary)
            data.to_csv('Password_file.csv', mode='a', index=False, header=False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:", bg=YELLOW, )
website_label.grid(column=0, row=1)

Email_label = Label(text="Email/Username:", bg=YELLOW, )
Email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=YELLOW, )
password_label.grid(column=0, row=3)

# Entry

website_entry = Entry(width=35)
# entry.insert(END,string='type here')
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(END, string='balasabkaguru@gmail.com')
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
# entry.insert(END,string='type here')
password_entry.grid(column=1, row=3)

# Button
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
