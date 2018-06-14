import pandas as pd
import sqlite3

conn=sqlite3.connect("factbook.db")

cursor=conn.cursor()
query="Select * from sqlite_master where type='table';"
cursor.execute(query)
table_results_sl=cursor.fetchall()
print(table_results_sl)
table_results_pd=pd.read_sql_query(query,conn)
print(table_results_pd)