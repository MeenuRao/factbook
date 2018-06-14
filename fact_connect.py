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

query_fact_tbl="select * from facts limit 5;"
print(pd.read_sql_query(query_fact_tbl,conn))
##Write a single query that returns the:

##minimum population
#maximum population
#minimum population growth
#maximum population growth
query_min="select min(population) from facts;"
query_max="select max(population) from facts;"

print("The min population")
print(pd.read_sql_query(query_min,conn))
print("The max population")
print(pd.read_sql_query(query_max,conn))

# Write a query that returns the countrie(s) with a population of 7256490011  7256490011.

query_country="select name from facts where population=32564342;"
#query_country="select * from facts where name = 'World'"
print("the country with population 7256490011")
print(pd.read_sql_query(query_country,conn))
