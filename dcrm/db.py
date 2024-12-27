# install mysql 
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector 
# pip install mysql-connector-python

# troubleshooting technique
# uninstall both mysql-connector and mysql-connector-python 
# pip install mysql-connector-python

import mysql.connector 

dbinput = input("Enter db name: ")
print(f"Please confirm this is the correct name: {dbinput}")
resultinput = input("Y or N").lower
if resultinput == 'y' or resultinput == 'yes':
    try: 
        # creating a database connection 
        dataBase = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Password1?'
        )

        # prepare a cusor object 
        cursorObect = dataBase.cursor()

        # create db 
        cursorObect.execute("CREATE DATABASE testco")
        print("datbase created ")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
else:
    dbinput = input("Enter db name: ")
    print(f"Please confirm this is the correct name: {dbinput}")
    resultinput = input("Y or N").lower
    break