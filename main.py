from register import *
from Bank import *
from Database import *
from Customers import *

status = False
print("-------------------------- Welcome To ScriptSafe Bank---------------------------")
while True:
    try:
        register = int(input("1. SignUp\n"
                            "2. SignIn\n"
                            "Please Enter Your Choice: "))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                user = SignIn()
                status = True
                break
        else:
            print("Please Enter Valid Input From Options")
    except ValueError:
        print("Invalid Input Try Again with Numbers")

account_number = db_query(
    "SELECT account_number FROM customers WHERE username = %s", (user,)
)[0][0]

while status:
    print(f"Welcome {user.capitalize()} Choose Your Banking Service\n")
    try:
        facility = int(input("1. Balance Enquiry\n"
                            "2. Cash Deposit\n"
                            "3. Cash Withdraw\n"
                            "4. Fund Transfer\n"
                            "5. Exit\n"
                            "Please Enter Your Choice: "))
        if facility >= 1 and facility <= 5:
            if facility == 1:
                bobj = Bank(user, account_number)
                bobj.balanceequiry()
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit: "))
                        bobj = Bank(user, account_number)
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter Amount to Withdraw: "))
                        bobj = Bank(user, account_number)
                        bobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number: "))
                        amount = int(input("Enter Money to Transfer: "))
                        bobj = Bank(user, account_number)
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 5:
                print("Thanks For Using Banking Services")
                status = False
        else:
            print("Please Enter Valid Input From Options")
            continue
    except ValueError:
        print("Invalid Input Try Again with Numbers")
        continue