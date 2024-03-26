from connection import MySQLConnection
from DBServices import *


def main():
    my_sqlconnection = sql_connect()
    accept_data(my_sqlconnection)
    sql_close(my_sqlconnection)


def sql_connect():
    try:
        mysql_connection = MySQLConnection('127.0.0.1', 'root', '1111', 'python2')

        mysql_connection.connect()

        return mysql_connection

    except Exception as e:
        print(f"Error connecting to python2 database")


def accept_data(mysql_connection):
    cursor = mysql_connection.cursor
    db = CarData()
    cursor.execute(db.car_select())

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    while True:
        usr_des = input("Would you like to add a new car to the table? (Y/N) ")

        if usr_des == "Y":
            if car_details(db):
                cursor.execute(db.car_insert(), (db.car_id, db.make, db.model, db.year))
                print("Successfully Added Data")
                break
        else:
            print("Error, enter data again")

        mysql_connection.connection.commit()


def sql_close(mysql_connection):
    mysql_connection.close()


def cat_details(cardata):
    usr_c_id = input("Enter Car ID")
    usr_make = input("Enter Car Make")
    usr_model = input("Enter Car Model")
    usr_year = input("Enter Year")


    cardata.car_construct(car_insert(), usr_c_id, usr_make, usr_model, usr_year)
    return True


main()
