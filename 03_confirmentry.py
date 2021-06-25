# Name: 03_confirmentry.py

# Purpose: This script confirms whether entries have been made into the DB today

# Date: 25/06/2021

# Author: Moses Otieno

# ---- Import modules
import datetime
import smtplib
from datetime import date
from email.message import EmailMessage
from mysql.connector import MySQLConnection
from python_mysql_dbconfig import read_db_config

# ---- Configure the databases

db_config = read_db_config()

conn = MySQLConnection(**db_config)

cursor = conn.cursor()

mycursor = conn.cursor()

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
tomorrow_date = todays_date + step
tomorrow_date = tomorrow_date.strftime('%d-%B-%Y')

# Configure the email

msg = EmailMessage()

msg['Subject'] = 'Meter Reading'
msg['From'] = "Moses Otieno"
msg['To'] = 'mosotieno25@gmail.com'

msg.set_content("Hello sir, " + "\n"
                                "This is to remind  you that you have not taken the meter readings "
                                "for KPLC and KIWASCO" + "\n\n"
                                                         "Moses Data")

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('mosedata2021@gmail.com', "J@yalo100")

if todays_date not in entries:
    server.send_message(msg)
else:
    print(f"The entry has been made check again on {tomorrow_date}")
