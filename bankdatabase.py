import mysql.connector

mydb = mysql.connector.connect(host ='localhost',user ='root',password='meenu')

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
mycursor = mydb.cursor()

## creating a databse called 'datacamp'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create tha 'bank' database
mycursor.execute("CREATE DATABASE bank")
