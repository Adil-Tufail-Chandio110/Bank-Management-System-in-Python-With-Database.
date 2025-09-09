from Database import *
class Customer:
 def __init__(self, user, password, name,age, city, account_number):
         self.__username = user
         self.__password = password
         self.__name = name
         self.__age = age
         self.__city = city
         self.__account_number = account_number

 def createUser(self):
     query = (
         "INSERT INTO customers (username, password, name, age, city, balance, account_number, status) "
         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
     )
     params = (
         self.__username, self.__password, self.__name, self.__age,
         self.__city, 0, self.__account_number, 1
     )
     db_query(query, params)
     mydb.commit()



