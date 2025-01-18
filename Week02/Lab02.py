
# 1. Name:
#      Tristin Parker
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program reads usernames and passwords from a JSON file,
#      prompts the user for their credentials, and checks if they are authenticated.
# 4. What was the hardest part? Be as specific as possible.
#      Going back and commenting throughout the assignment. With simple programs like this, I find myself not commenting where I should, and like I do with more complex programs.
#      I need to get back in the habbit of commenting as I go no matter what.
# 5. How long did it take for you to complete the assignment?
#      Writing assignment - 25 minutes, adding comments - 5 minutes, Recording video - 8 Minutes
#      Total time - 38 Minutes
import json

# Attempt to open the JSON file and load the data
try:
    with open('Lab02.json', 'r') as file:
        data = json.load(file)
        usernames = data['username']
        passwords = data['password']
        print("Enter a correct username & password to find out a secret!")  # Added a fun message
except FileNotFoundError:
    print("Unable to open file Lab02.json.")
    exit()

# Initialize variables for authentication attempts
max_attempts = 3  # Allows the user 3 attempts (because I hate programs that exit after 1 fail)
attempts = 0

# Loop until the user is authenticated or exceeds the maximum attempts
while attempts < max_attempts:
    username = input("Username: ")
    password = input("Password: ")

    authenticated = False
    for i in range(len(usernames)):
        if username == usernames[i] and password == passwords[i]:
            authenticated = True
            break

    if authenticated:
        print("You are authenticated!")
        print("The secret is that coding is awesome!")  # Reveal the secret message
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"You are not authorized to use the system. You have {remaining_attempts} attempts remaining.")

if not authenticated:
    print("Too many incorrect attempts. Program terminated.")