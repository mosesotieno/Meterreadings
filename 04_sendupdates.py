# Name: 04_sendupdates.py

# Purpose: This script sends weekly updates on the readings

# Date: 29/06/2021

# Author: Moses Otieno

# ---- Import modules
import smtplib
from datetime import date, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from mysql.connector import MySQLConnection
from python_mysql_dbconfig import read_db_config

# ---- Configure the databases

db_config = read_db_config()

conn = MySQLConnection(**db_config)

kplcdata = pd.read_sql_query("SELECT entry_date, reading FROM kplcreading", conn)
kiwascodata = pd.read_sql_query("SELECT entry_date, reading FROM kiwascoreading", conn)

kiwascodata['date_read'] = pd.to_datetime(kiwascodata.entry_date).dt.strftime('%d-%B-%Y')
kplcdata['date_read'] = pd.to_datetime(kplcdata.entry_date).dt.strftime('%d-%B-%Y')

kiwascodata['entry_date'] = pd.to_datetime(kiwascodata.entry_date).dt.date
kplcdata['entry_date'] = pd.to_datetime(kplcdata.entry_date).dt.date


# Extract the dates to send the updates

def get_first_day(dt, d_years=0, d_months=0):
    # d_years, d_months are "deltas" to apply to dt
    y, m = dt.year + d_years, dt.month + d_months
    a, m = divmod(m - 1, 12)
    return date(y + a, m + 1, 1)


def get_last_day(dt):
    return get_first_day(dt, 0, 1) + timedelta(-1)


todays_date = date.today()  # Todays dates

firstdate = get_first_day(todays_date)
lastdate = get_last_day(todays_date)


def filterdata(data):
    after_start_date = data["entry_date"] >= firstdate
    before_end_date = data["entry_date"] <= lastdate
    between_two_dates = after_start_date & before_end_date
    filtered_dates = data.loc[between_two_dates]
    return filtered_dates


kplcdata = filterdata(kplcdata)
kiwascodata = filterdata(kiwascodata)

kplcdata = kplcdata[['date_read', 'reading']]
kiwascodata = kiwascodata[['date_read', 'reading']]

# Configure the Email

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('mosedata2021@gmail.com', "J@yalo100")

recipients = ['mosotieno25@gmail.com']
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = "Meter Readings"
msg['From'] = 'mosedata2021@gmail.com'


# Readings in the list

def sendhtml(reading):
    html = """\
    <html>
      <head>The readings for KPLC and KIWASCO</head>
      <body>
        {0}
      </body>
    </html>
    """.format(reading.to_html())

    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    server.sendmail(msg['From'], emaillist, msg.as_string())


if todays_date != lastdate:
    sendhtml(kplcdata)
    sendhtml(kiwascodata)
else:
    print(f"The readings will be sent on {lastdate}")
