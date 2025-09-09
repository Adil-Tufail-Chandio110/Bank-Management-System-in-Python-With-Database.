import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    password="Virgil123!@#",
    database="Bank"
)
cursor = mydb.cursor()

def db_query(query, params=()):
    cursor.execute(query, params)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers
        (username VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL,
        name VARCHAR(20) NOT NULL,
        age INTEGER NOT NULL,
        city VARCHAR(20) NOT NULL,
        balance INTEGER NOT NULL,
        account_number INTEGER NOT NULL,
        status BOOLEAN NOT NULL)
    ''')

def createtransactiontable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions
        (timedate VARCHAR(30),
        account_number INTEGER,
        remarks VARCHAR(30),
        amount INTEGER,
        username VARCHAR(20))
    ''')

mydb.commit()

if __name__ == "__main__":
    createcustomertable()
    createtransactiontable()