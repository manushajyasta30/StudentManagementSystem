"""
This is a Welcome Page
"""

from User_Menu import show_user_menu
import hashlib
import re


class UserManagement:
    def __init__(self):
        self.users = {'Harry': '@Password'}  # Dictionary to store username-password pairs

    def register_user(self):
        print('===========================Registration=============================')
        print('\u2666 Account Name is between 3 and 6 letters long')
        print('\u2666 Account name\'s first letter must be capitalized')
        while True:
            username = input("Enter a username: ")
            username_validity = self.is_valid_username(username)
            if username_validity == "invalid_format":
                print("\u274C Account Name Not Valid!")
                continue
            elif username_validity == "exists":
                print("\u274C Registration Failed! Account Already Exists")
                print("\n===============================================\n")
                break

            print('\u2666 Password must start with one of the following special characters !@#$%^&*')
            print('\u2666 Password must contain at least one digit, one lowercase letter, and one uppercase letter')
            print('\u2666 Password is between 6 and 12 characters long')
            while True:
                password = input("Please Enter your password: ")
                if not self.is_valid_password(password):
                    print("\u274C Password Not Valid!")
                    continue

                # Hashing the password before saving
                hashed_password = hashlib.md5(password.encode()).hexdigest()

                # If all conditions are met, register the user
                self.users[username] = hashed_password
                print("\u2714 Registration Completed!")
                print('\n==========================================================\n')
                return

    def is_valid_username(self, username):
        if not re.match("^[A-Z][a-zA-Z]{2,5}$", username):
            return "invalid_format"
        if username in self.users:
            return "exists"
        return True

    def is_valid_password(self, password):
        if not (6 <= len(password) <= 12):
            return False
        if not re.search("[A-Z]", password) or not re.search("[a-z]", password) or not re.search("[0-9]", password):
            return False
        if not password[0] in "!@#$%^&*":
            return False
        return True

    def login(self):
        print('=========================Login============================')
        while True:
            username = input("Please Enter Your Account: ")
            if username not in self.users:
                print('\u274C Login Failed! Account Not Exists')
                continue
            while True:
                password = input("Please Enter your password: ")
                if not (self.users[username] == password):
                    print('\u274C Login Failed! Invaid Password')
                    continue
                show_user_menu(username)


# Usage example
user_manager = UserManagement()

# Welcome page (content loaded from welcome.txt)
with open("welcome.txt", "r") as file:
    welcome_content = file.read()
    print(welcome_content)

while True:
    choice = input("Please Enter(1-3):")
    if choice == '1':
        user_manager.login()
    elif choice == '2':
        user_manager.register_user()
    elif choice == '3':
        exit()
    else:
        print("Invalid choice. Please enter '1' or '2'.")
