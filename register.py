# User Registration Signin Signup
from Customers import *
from Bank import Bank
import random
from Database import db_query, createtransactiontable

def SignUp():
    while True:
        username = input("Create Username: ")
        temp = db_query("SELECT username FROM customers WHERE username = %s", (username,))
        if temp:
            print("Username Already Exists")
            continue
        else:
            print("Username is Available Please Proceed")
            break
    password = input("Enter Your Password: ")
    name = input("Enter Your Name: ")
    try:
        age = int(input("Enter Your Age: "))
    except ValueError:
        print("Age must be a number")
        return
    city = input("Enter Your City: ")
    while True:
        account_number = random.randint(10000000, 99999999)
        temp = db_query("SELECT account_number FROM customers WHERE account_number = %s", (account_number,))
        if temp:
            continue
        else:
            print("Your Account Number", account_number)
            break
    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createUser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()  # This is now a no-op, but kept for compatibility

def SignIn():
    username = input("Enter Username: ")
    temp = db_query("SELECT username FROM customers WHERE username = %s", (username,))
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} Enter Password: ")
            temp = db_query("SELECT password FROM customers WHERE username = %s", (username,))
            if temp[0][0] == password:
                print("Sign IN Successfully")
                return username
            else:
                print("Wrong Password Try Again")
                continue
    else:
        print("Enter Correct Username")
        SignIn()