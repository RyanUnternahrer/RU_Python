import os.path

print("Welcome to Ryan's password manager.")
userChoice = input("Choose one: (1) make/check integerity of file (2) append new password (3) read file: ")
userChoice = int(userChoice)

if userChoice == 1:
    checkExistacne()
elif userChoice == 2:
    appendNew()
elif userChoice == 3:
    readPasswords()
else:
    print("invalid responce")

def checkExistacne():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()

def appendNew():
    # This function will append new password in the txt file
    file = open("info.txt", 'a')

    print()
    print()

    userName = input("Please enter the user name: ")
    password = input("Please enter the password here: ")
    website = input("Please enter the website address here: ")

    print()
    print()

    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close

def readPasswords():
    file = open('info.txt', 'r')
    content = file.read()
    file.close()
    print(content)
