import sheety  # Importing the sheety module

# Welcome message
print("Welcome to Catkat's Flight Club.")
print("We find the best deals and email you.")

# Asking for user information
first_name = input("What's your first name?\n")
last_name = input("What's your last name?\n")
email = input("What is your email?\n")
email_check = input("Type your email again.\n")

# Checking if email confirmation matches
if email == email_check:
    print("You're in the club!")  # Confirmation message
    # Adding user data to the sheet via the post_new_row function from the sheety module
    sheety.post_new_row(first_name, last_name, email)
