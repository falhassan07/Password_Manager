from tkinter import * 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(width=800, height=600, padx=20, pady=20)
window.title("Password Manager")


canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)


website_label = Label(text="Website: ")
# website_label.config(padx=30)
website_label.grid(column=0, row=1)


email_username_label = Label(text="Email/Username: ")
# email_username_label.config(padx=30)
email_username_label.grid(column=0, row=2)


password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)


website_input = Entry(width=40)
website_input.grid(column=1,row=1)

email_username_input = Entry(width=40, text="helo@gmail.com")
email_username_input.grid(column=1,row=2)
email_username_input.insert(END, string="example@email.com")


password_input = Entry()
password_input.grid(column=1,row=3)


password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)


add_button = Button(text="Add", width=38)
add_button.grid(column=1, row=4)














window.mainloop()