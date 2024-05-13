# database.py

import mysql.connector


def connect_to_database():
    return mysql.connector.connect(
        host="127.0.0.1", user="root", passwd="123sumit", database="Hospital"
    )


def create_database():
    connect_to_database = mysql.connector.connect(
        host="127.0.0.1", user="root", passwd="123sumit"
    )
    cursor = connect_to_database.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Hospital")
    cursor.close()
    connect_to_database.close()


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Patient(
            Patient_ID INT AUTO_INCREMENT PRIMARY KEY,
            room_id INT,
            Patient_Name VARCHAR(255),
            Patient_Address VARCHAR(255),
            Patient_Phone VARCHAR(255),
            Patient_Disease VARCHAR(255)
        )
    """
    )
    cursor.close()
