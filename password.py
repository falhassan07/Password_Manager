from tkinter import * 
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)


add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4,columnspan=2)


window.mainloop()