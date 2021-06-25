# Name: 00_createtables.py

# Purpose: Creates tables for KPLC and KIWASCO

# Date: 24/06/2021

# Author: Moses Otieno

# ---- Import modules

from mysql.connector import MySQLConnection
from python_mysql_dbconfig import read_db_config


# ---- Configure the databases

db_config = read_db_config()

conn = MySQLConnection(**db_config)

mycursor = conn.cursor()

# ---- Create the table for KPLC readings

mycursor.execute("CREATE TABLE IF NOT EXISTS kplcreading"
                 "(id INT AUTO_INCREMENT PRIMARY KEY, "
                 "entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP," 
                 "reading INT NOT NULL CHECK (reading>=293000))")

# ---- Create the table for KIWASCO readings

mycursor.execute("CREATE TABLE IF NOT EXISTS kiwascoreading"
                 "(id INT AUTO_INCREMENT PRIMARY KEY, "
                 "entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP," 
                 "reading INT NOT NULL CHECK (reading>=5867543))")
