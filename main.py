from tkinter import *
from tkinter import messagebox, simpledialog
import random
import pyperclip
import json

def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = simpledialog.askinteger("Enter quantity of letters","How many letters would you like in your password?", minvalue=6,maxvalue=len(letters))
    window.update()
    nr_symbols = simpledialog.askinteger("Enter quantity of symbols","How many symbols would you like in your password?", minvalue=4,maxvalue=len(symbols))
    window.update()
    nr_numbers = simpledialog.askinteger("Enter quantity of numbers","How many numbers would you like in your password?", minvalue=4,maxvalue=len(numbers))

    rand_letters = [letters[random.randint(0,len(letters)-1)] for letters[random.randint(0,len(letters)-1)] in range(0,nr_letters)]
    rand_symb = [symbols[random.randint(0,len(symbols)-1)] for symbols[random.randint(0,len(symbols)-1)] in range(0,nr_symbols)]
    rand_num = [numbers[random.randint(0,len(numbers)-1)] for numbers[random.randint(0,len(numbers)-1)] in range(0,nr_numbers)]
    rand_pass = rand_letters + rand_symb + rand_num
    random.shuffle(rand_pass)
    password = "".join([str(i) for i in rand_pass])
    password_entry.insert(0,password)
    pyperclip.copy(password)

def save_to_file():
    new_data = {
        website_entry.get():
        {
            "email:": username_entry.get(),
            "password:":password_entry.get(),
        }

        }
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo("Empty field/s detected", "Please do not leave empty entry.")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                data.update(new_data)
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        website_entry.delete(0,END)
        password_entry.delete(0,END)
def search_website():
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            if f"{website_entry.get()}" in data.keys():
                email = data[f"{website_entry.get()}"]["email:"]
                password = data[f"{website_entry.get()}"]["password:"]
                messagebox.showinfo(f"{website_entry.get()}:",f"Email/Username: {email}\nPassword: {password}")
            else:
                messagebox.showinfo("No entries found in file","There are no an entries for that specific website.\nFirst provide proper data.")
    except FileNotFoundError:
        messagebox.showinfo("FileNotFoundError", "There is no file created to search in")

window = Tk()
window.title("Password Manager")
window.minsize(800,600)
window.config(padx=20,pady=20,bg="black")
canvas = Canvas(width=512, height=512, bg="black",highlightthickness=0)
lock_image = PhotoImage(file="password-manager-icon-18.png")
canvas.create_image(230, 240, image=lock_image, anchor="center")
canvas.grid(column=1,row=0)
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
website_entry = Entry(width=81)
website_entry.focus()
website_entry.grid(column=1,row=1,padx=40)
username_label = Label(text="Email/Username:")
username_label.grid(column=0,row=2)
username_entry = Entry(width=65)
username_entry.insert(0, "example@gmail.com")
username_entry.grid(column=0,row=2,columnspan=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)
password_entry = Entry(width=65)
password_entry.grid(column=0, row=3,columnspan=2)
generate_button = Button(text="Generate Password", width=20,command=generator)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=50,command=save_to_file)
add_button.grid(column=0, row=4, columnspan=2)
search_button = Button(text="Search", width=20,command=search_website)
search_button.grid(column=2,row=1)


window.mainloop()
