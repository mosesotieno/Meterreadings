# Name: 03_confirmentry.py

# Purpose: This script confirms whether entries have been made into the DB today

# Date: 25/06/2021

# Author: Moses Otieno

# ---- Import modules
import datetime
from datetime import date
import smtplib
from email.message import EmailMessage
from datetime import datetime
from mysql.connector import MySQLConnection
from python_mysql_dbconfig import read_db_config

# ---- Configure the databases

db_config = read_db_config()

conn = MySQLConnection(**db_config)

cursor = conn.cursor()

mycursor = conn.cursor()

# Pull the entry_dates from the table

mycursor.execute("SELECT entry_date FROM kplcselfreading")

kplcentries = mycursor.fetchall()

allentries = kplcentries

# Convert the entries from tuples to dates and store in a list
entries = []

for i in allentries:
    for j in i:
        entries.append(j)

entries = list(set(entries))

monthentries = []
for j in entries:
    monthentries.append(j.month)


# Todays date

def last_day_of_month(year, month):
    """ Work out the last day of the month """
    last_days = [31, 30, 29, 28, 27]
    for day in last_days:
        try:
            end = datetime(year, month, day)
        except ValueError:
            continue
        else:
            return end.date()
    return None


todays_date = date.today()
cyear = todays_date.year
cmonth = todays_date.month
lastday = last_day_of_month(cyear, cmonth)
monthname = todays_date.strftime('%B')

# Configure the email

msg = EmailMessage()

msg['Subject'] = 'KPLC Self Reading Submission'
msg['From'] = "Moses Otieno"
msg['To'] = 'mosotieno25@gmail.com'

msg.set_content("Hello sir, " + "\n"
                "This is to remind  you that you have not submited KPLC readings "
                + "\n\n" +
                  "Moses Data")

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('mosedata2021@gmail.com', "J@yalo100")


if cmonth not in monthentries and todays_date == lastday:
    server.send_message(msg)
else:
    print(f"The reading for {monthname} already submitted.")
