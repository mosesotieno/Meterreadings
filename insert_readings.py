# Name: insert_readings.py

# Purpose: This script inserts the Meter readings into the appropriate
#          tables

# Date: 24/06/2021

# Author: Moses Otieno

# ---- Import modules

from mysql.connector import MySQLConnection
from python_mysql_dbconfig import read_db_config
from datetime import date
import datetime

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


# First check whether entry has been made for the day

# Pull the entry_dates from the table

mycursor.execute("SELECT entry_date FROM kplcreading")

kplcentries = mycursor.fetchall()

mycursor.execute("SELECT entry_date FROM kiwascoreading")

kiwascoentries = mycursor.fetchall()

allentries = kplcentries + kiwascoentries

# Convert the entries from tuples to dates and store in a list
entries = []

for i in allentries:
    for j in i:
        entries.append(j.date())

entries = list(set(entries))

# Todays date

todays_date = date.today()  # Todays dates

step = datetime.timedelta(days=1)

if todays_date not in entries:
    enter_details()
else:
    print(f"The entry has been made check again on {todays_date + step}")
