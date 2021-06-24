# Name: insert_readings.py

# Purpose: This script inserts the Meter readings into the appropriate
#          tables

# Date: 24/06/2021

# Author: Moses Otieno

# ---- Import modules

from mysql.connector import MySQLConnection
from python_mysql_dbconfig import read_db_config

# ---- Configure the databases

db_config = read_db_config()

conn = MySQLConnection(**db_config)

cursor = conn.cursor()

mycursor = conn.cursor()

companys = ["KIWASCO", "KPLC"]


def enter_details():
    for company in companys:
        if company == "KPLC":
            kplcreading = input(f"What is the KPLC reading today? ")
            sql = f"INSERT INTO kplcreading(reading) VALUES ({kplcreading})"
            val = kplcreading
            mycursor.execute(sql, val)
            conn.commit()
        elif company == "KIWASCO":
            kiwascoreading = input("What is the KIWASCO reading today? ")
            sql = f"INSERT INTO kiwascoreading(reading) VALUES ({kiwascoreading})"
            val = kiwascoreading
            mycursor.execute(sql, val)
            conn.commit()


enter_details()
