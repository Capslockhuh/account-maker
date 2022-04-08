# accounts.py - program to make/log into accounts and save data to them

import logging
import pyinputplus

def createAccount():
    global login
    login = input('Please choose a login.\n')
    print('Please choose a password')
    global password
    password = pyinputplus.inputPassword()
    
choice = input('Account maker\nPress 1 to log into an account\nPress 2 to create a new account\n')
if choice == '1':
    enteredLogin = input('Please enter your login.\n')
    if enteredLogin == login:
        print('Please enter your password.\n')
        enteredPassword = pyinputplus.inputPassword()
        if enteredPassword == password:
            print('Logged succesfully.\n Current account:' + login)
    else:
        print('Invalid login.\n ')
        enteredLogin = input('Please enter your login.\n')
elif choice == '2':
    createAccount()
    choice = input('Account maker\nPress 1 to log into an account\nPress 2 to create a new account\n')
else:
    print('Please choose a valid option:\nPress 1 to log into an account\nPress 2 to create a new account\n')

