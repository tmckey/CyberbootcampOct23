# Today we are going to create a random password generator using for loops and arrays in python
# Make sure to print you password to the screen
#Can you randomize your password generated

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# # What is line 15 doing?
# password = []
# # Below is the guide how to write the for loop you need to write for symbols and numbers
# for char in range(1, nr_letters + 1):
#     password.append(random.choice(letters))

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

# Loop for letters
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))

# Loop for symbols
for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

# Loop for numbers
for char in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

# Shuffle the password to randomize the order
random.shuffle(password)

# Convert the list to a string
password_str = ''.join(password)

# Print the generated password
print("Generated Password:", password_str)


# import random

# # Define arrays of characters
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# digits = '0123456789'
# special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'

# # Combine all characters
# all_characters = uppercase_letters + lowercase_letters + digits + special_characters

# # Set the length of the password
# password_length = 12  # You can adjust the length as needed

# # Initialize an empty password
# password = ''

# # Generate the password using a for loop
# for _ in range(password_length):
#     password += random.choice(all_characters)

# # Print the generated password
# print("Random Password:", password)
    
# import random

# # Define arrays of characters
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# digits = '0123456789'
# special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'

# # Combine all characters
# all_characters = uppercase_letters + lowercase_letters + digits + special_characters

# # Set the length of the password
# password_length = 12  # You can adjust the length as needed

# # Generate the password using list comprehension
# password = ''.join(random.choice(all_characters) for _ in range(password_length))

# # Print the generated password
# print("Random Password:", password)