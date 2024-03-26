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
        print(f"Error connecting to cats database")


def accept_data(mysql_connection):
    cursor = mysql_connection.cursor
    db = CatsData()
    cursor.execute(db.cats_select())

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    while True:
        usr_des = input("Would you like to add a new cat to the table? (Y/N) ")

        if usr_des == "Y":
            if cat_details(db):
                cursor.execute(db.cats_insert(), (db.cat_id, db.owner_id, db.name, db.breed, db.age))
                print("Successfully Added Data")
                break
        else:
            print("Error, enter data again")

        mysql_connection.connection.commit()


def sql_close(mysql_connection):
    mysql_connection.close()


def cat_details(catsdata):
    usr_c_id = input("Enter Cat ID")
    usr_o_id = input("Enter Owner ID")
    usr_name = input("Enter Name")
    usr_breed = input("Enter Breed")
    usr_age = input("Enter Age")

    catsdata.cats_construct(usr_c_id,
                            usr_o_id,
                            usr_name,
                            usr_breed,
                            usr_age)

    return True


main()
