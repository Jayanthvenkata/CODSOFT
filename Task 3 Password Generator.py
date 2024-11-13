import string
import random

pass_length = int(input("Enter password length: "))

print('''Choose the type of password :
        1. Digits
        2. Letters
        3. Special characters
        4. Exit''')

characterList = ""
while(True):

    number = int(input("Pick a number "))
    if (number == 1):
        characterList += string.punctuation
    elif (number == 2):
        characterList += string.digits
    elif (number== 3):
        characterList += string.ascii_letters
    elif (number == 4):
        break
    else:
        print("Please choose a valid option!!!!")
password = []
for a in range (pass_length):
    randomchar = random.choice (characterList)
    password.append(randomchar)
print("The random password is " + "".join(password))
