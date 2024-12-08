# <b>Password Manager App </b>
## <b>Overview </b>
This project is a simple and secure Password Manager built with Python and the Tkinter library for the graphical user interface (GUI). The app helps you securely manage your credentials by storing website, email/username, and password data locally. It also includes a password generator to create strong, random passwords.

## Features
1. Password Generator:
    - Automatically generates strong, random passwords using a mix of letters, numbers, and symbols.
    - Copies the generated password to your clipboard for easy pasting.
2. Data Saving:
    - Saves website, email/username, and password details to a local data.txt file.
    - Prompts the user for confirmation before saving the data.
3. User-Friendly Interface:
    - Easy-to-use graphical interface created with Tkinter.
    - Minimal and straightforward layout.

## How to Use
1. Generate a Password:
    - Click the "Generate Password" button to create a strong, secure password.
    - The generated password is automatically copied to your clipboard.
2. Save Credentials:
    - Enter the website, email/username, and password into the respective input fields.
    - Click "Add" to save the credentials. The data will be appended to the data.txt file.
3. Local Storage:
    - All credentials are stored locally in the data.txt file in the following format:
    
## Requirements
    - Python 3.x
    - Libraries:
        - tkinter (for GUI)
        - pyperclip (for clipboard functionality)

## Setup and Running the App
1. Clone or download the project files.
2. Place the logo.png file in the same directory as the script.
3. ### Run the script:
        python password_manager.py

## Future Enhancements
1. Add encryption for the stored passwords.
2. Implement database storage for improved data management.