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
                 "reading INT NOT NULL CHECK (reading>=586754))")

# ----- Create the self-reading table and actual cost

mycursor.execute("CREATE TABLE IF NOT EXISTS kplcselfreading"
                 "(id INT AUTO_INCREMENT PRIMARY KEY, "
                 "entry_date DATE," 
                 "start_date DATE,"
                 "end_date DATE,"
                 "reading INT NOT NULL,"
                 "consumption INT NOT NULL,"
                 "cost DOUBLE(6,2) NOT NULL)")
