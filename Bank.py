# Bank Services
from Database import *
import datetime

class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number

    def create_transaction_table(self):
        # No need to create a user-specific table; the single transactions table is created in Database.py
        pass

    def balanceequiry(self):
        temp = db_query(
            "SELECT balance FROM customers WHERE username = %s",
            (self.__username,)
        )
        print(f"{self.__username} Balance is {temp[0][0]}")

    def deposit(self, amount):
        temp = db_query(
            "SELECT balance FROM customers WHERE username = %s",
            (self.__username,)
        )
        test = amount + temp[0][0]
        db_query(
            "UPDATE customers SET balance = %s WHERE username = %s",
            (test, self.__username)
        )
        self.balanceequiry()
        db_query(
            "INSERT INTO transactions (timedate, account_number, remarks, amount, username) "
            "VALUES (%s, %s, %s, %s, %s)",
            (str(datetime.datetime.now()), self.__account_number, "Amount Deposit", amount, self.__username)
        )
        print(f"{self.__username} Amount is Successfully Deposited into Your Account {self.__account_number}")

    def withdraw(self, amount):
        temp = db_query(
            "SELECT balance FROM customers WHERE username = %s",
            (self.__username,)
        )
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            test = temp[0][0] - amount
            db_query(
                "UPDATE customers SET balance = %s WHERE username = %s",
                (test, self.__username)
            )
            self.balanceequiry()
            db_query(
                "INSERT INTO transactions (timedate, account_number, remarks, amount, username) "
                "VALUES (%s, %s, %s, %s, %s)",
                (str(datetime.datetime.now()), self.__account_number, "Amount Withdraw", amount, self.__username)
            )
            print(f"{self.__username} Amount is Successfully Withdrawn from Your Account {self.__account_number}")

    def fundtransfer(self, receive, amount):
        temp = db_query(
            "SELECT balance FROM customers WHERE username = %s",
            (self.__username,)
        )
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            temp2 = db_query(
                "SELECT balance FROM customers WHERE account_number = %s",
                (receive,)
            )
            if not temp2:
                print("Account Number Does not Exist")
            else:
                test1 = temp[0][0] - amount
                test2 = amount + temp2[0][0]
                db_query(
                    "UPDATE customers SET balance = %s WHERE username = %s",
                    (test1, self.__username)
                )
                db_query(
                    "UPDATE customers SET balance = %s WHERE account_number = %s",
                    (test2, receive)
                )
                receiver_username = db_query(
                    "SELECT username FROM customers WHERE account_number = %s",
                    (receive,)
                )[0][0]
                self.balanceequiry()
                db_query(
                    "INSERT INTO transactions (timedate, account_number, remarks, amount, username) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (str(datetime.datetime.now()), self.__account_number, f"Fund Transfer -> {receive}", amount, self.__username)
                )
                db_query(
                    "INSERT INTO transactions (timedate, account_number, remarks, amount, username) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (str(datetime.datetime.now()), receive, f"Fund Transfer From {self.__account_number}", amount, receiver_username)
                )
                print(f"{self.__username} Amount is Successfully Transferred from Your Account {self.__account_number}")