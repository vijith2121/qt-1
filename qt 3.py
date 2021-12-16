import sqlite3
from sqlite3 import Error
import csv


def create_db():
    try:
        con = sqlite3.connect("test.db")
        con.execute('''CREATE TABLE employees
         (SL_NO INT PRIMARY KEY NOT NULL,
         First_Name TEXT NOT NULL,
         Second_Name TEXT NOT NULL,
         Gender TEXT NOT NULL,
         Bith_Date DATE NOT NULL,
         AGE INT NOT NULL,
         Annual_Salary INT NOT NULL);''')

    except Error as e:
        print(e)
    finally:
        if con:
            con.close()


# create_db()

with open('employee_info.csv') as data:
    csvfile = csv.reader(data)
    data = []
    for i in csvfile:
        data.append(i)
