#Contraseña y usuario
User= "Carlos"
Password= "1234"

Us= input("Please enter your username: ")
Pass= input("Please enter your password: ")


if Us != User:
    print("The username is unvalible")
elif Pass != Password:
    print("The password is unvalible")
else:
    print("Welcome to the account Carlos")