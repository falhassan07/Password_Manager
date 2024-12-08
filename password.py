from random import choice, randint, shuffle
from tkinter import * 
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_input.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    #list to store password characters
    password_list = password_letters + password_symbols + password_numbers


    #shuffle values of password_list
    shuffle(password_list)

    #join password values
    password = ''.join(password_list)

    password_input.insert(END, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please do not leave any fileds empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the detials entereed: \nEmail: {email_username} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email_username} | {password}\n")
                website_input.delete(0, "end")
                password_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(width=800, height=600, padx=20, pady=20)
window.title("Password Manager")


canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)


# LABELS
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)


email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)


password_label = Label(text="Password:")
password_label.grid(column=0, row=3)




# INPUTS/ENTRIES
website_input = Entry(width=38)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()


email_username_input = Entry(width=38)
email_username_input.grid(column=1,row=2,columnspan=2)
email_username_input.insert(END, string="example@email.com")


password_input = Entry(width=21)
password_input.grid(column=1,row=3)


# BUTTONS
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)


add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4,columnspan=2)


window.mainloop()