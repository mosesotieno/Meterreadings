import pandas as pd
from mysql.connector import MySQLConnection
from python_mysql_dbconfig import read_db_config

db_config = read_db_config()

conn = MySQLConnection(**db_config)


def pulldata(data):
    dataset = pd.read_sql_query(f"SELECT entry_date, reading FROM {data}", conn)
    dataset['date_read'] = pd.to_datetime(dataset.entry_date).dt.strftime('%d-%B-%Y')
    dataset['entry_date'] = pd.to_datetime(dataset.entry_date).dt.date
    return dataset


def filterdata(data):
    dataset = data[['date_read', 'reading']]
    return dataset
