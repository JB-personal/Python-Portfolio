# ask user if they want to generate a password
# get the length of the password
# generate password
# show the user
# exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*():;?<>~{}[]")

def generate():
    password_length = int(input("How long do you want your password to be?: "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)



option = input("Would you like to generate a password? (Yes/No): ")

if option == "Yes":
    generate()
elif option == "No":
    print("Program ended")
    quit()
else:
    print("Invalid Imput")
    quit()