# Bank-Management-System-in-Python-With-Database.

# Overview:
The Bank Management System is a Python-based command-line application that simulates core banking operations. It allows users to sign up, sign in, and perform transactions such as balance inquiries, deposits, withdrawals, and fund transfers. The system uses a MySQL database to store customer information and transaction records, ensuring data persistence. This project demonstrates object-oriented programming, database integration, and user input handling in Python.
Features

# User Authentication:
Sign Up: Create a new account with a unique username, password, and randomly generated 8-digit account number.
Sign In: Log in using a username and password.


# Banking Operations:
Balance Inquiry: Check the current account balance.
Deposit: Add money to the user's account.
Withdrawal: Withdraw money with balance validation.
Fund Transfer: Transfer money to another account using the recipient's account number.


# Transaction Logging:
Records all transactions (deposits, withdrawals, transfers) with timestamps in a MySQL database.
Data Persistence: Stores customer details and transaction history in a MySQL database.
Input Validation: Handles invalid inputs (e.g., non-numeric values) with appropriate error messages.

#Prerequisites:

To run this project, you need:
Python 3.x installed on your system.
MySQL Server installed and running.
MySQL Connector for Python: Install using:pip install mysql-connector-python


A MySQL database named Bank with the following credentials (or modify Database.py to match your setup):
Host: localhost
User: root
Password: "Your Password"

Install Dependencies:Install the required Python library:pip install mysql-connector-python

Set Up the MySQL Database:
Ensure MySQL is running.
Create a database named Bank:CREATE DATABASE Bank;

#Usage

Run the Application:Execute the main script:
python main.py


Sign Up or Sign In:

Choose 1 to sign up and create a new account with details like username, password, name, age, city, and an initial balance of 0.
Choose 2 to sign in with an existing username and password.


Perform Banking Operations:After signing in, select from the following options:

1: Check your account balance.
2: Deposit money into your account.
3: Withdraw money (if sufficient balance is available).
4: Transfer funds to another account using the recipient's account number.
5: Exit the application.


Example Interaction:
-------------------------- Welcome To ScriptSafe Bank---------------------------
1. SignUp
2. SignIn
Please Enter Your Choice: 1
Create Username: johndoe
Username is Available Please Proceed
Enter Your Password: password123
Enter Your Name: John Doe
Enter Your Age: 30
Enter Your City: New York
Your Account Number: 12345678

Welcome Johndoe Choose Your Banking Service
1. Balance Enquiry
2. Cash Deposit
3. Cash Withdraw
4. Fund Transfer
5. Exit
Please Enter Your Choice: 2
Enter Amount to Deposit: 1000
johndoe Balance is 1000
johndoe Amount is Successfully Deposited into Your Account 12345678



Project Structure
bank-management-system/
│
├── main.py                # Main script to run the application
├── register.py            # Handles user sign-up and sign-in
├── Bank.py                # Implements banking operations (deposit, withdraw, transfer, balance inquiry)
├── Customers.py           # Manages customer data and account creation
├── Database.py            # Sets up MySQL database connection and table creation
├── temp.py                # Utility script for generating random account numbers
├── README.md              # This file
└── requirements.txt       # List of dependencies

Code Explanation

main.py: Entry point of the application, providing the user interface for sign-up, sign-in, and banking operations.
register.py: Contains SignUp and SignIn functions for user registration and authentication, generating unique account numbers.
Bank.py: Defines the Bank class with methods for balance inquiries, deposits, withdrawals, and fund transfers, interacting with the database.
Customers.py: Defines the Customer class to create and store customer details in the MySQL database.
Database.py: Establishes the MySQL connection, creates the customers and transactions tables, and provides a db_query function for database operations.
temp.py: A utility script to generate random 8-digit account numbers (used during development).

Database Schema

customers table:
username: VARCHAR(20), unique user identifier.
password: VARCHAR(20), user password.
name: VARCHAR(20), customer's name.
age: INTEGER, customer's age.
city: VARCHAR(20), customer's city.
balance: INTEGER, current account balance.
account_number: INTEGER, unique 8-digit account number.
status: BOOLEAN, account status (1 for active).


transactions table:
timedate: VARCHAR(30), timestamp of the transaction.
account_number: INTEGER, account involved in the transaction.
remarks: VARCHAR(30), description (e.g., "Amount Deposit").
amount: INTEGER, transaction amount.
username: VARCHAR(20), user associated with the transaction.



Notes

Ensure the MySQL server is running before executing the program.
The default database credentials in Database.py must match your MySQL setup, or the connection will fail.
The system validates inputs (e.g., numeric values for amounts) and checks for sufficient balance during withdrawals and transfers.
Transaction history is stored but not displayed in the current interface; you can extend the project to include a transaction history feature.

# Future Improvements:

Add a feature to display transaction history for users.
Implement password hashing for better security.
Add a graphical user interface (GUI) using Tkinter or another framework.
Include account deletion or deactivation functionality.
Add support for multiple account types (e.g., savings, checking).

# Contributing:
Contributions are welcome! To contribute:

# License: 
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or suggestions, feel free to reach out:

# GitHub:https://github.com/Adil-Tufail-Chandio110
# Email: channdioadiltufail@gmail.com
