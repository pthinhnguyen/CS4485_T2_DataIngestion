import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

#try:
#	conn = msql.connect(host='localhost', user='root',  password='password')#give ur username, password
#   if conn.is_connected():
#		cursor = conn.cursor()
		#cursor.execute('DROP TABLE IF EXISTS zipcode;')
#		cursor.execute("CREATE DATABASE zipcode")
#       print("Database is created")
#except Error as e:
#	print("Error while connecting to MySQL", e)
#empdata = pd.read_csv('zipcode.csv', index_col=False, delimiter = ',')
#empdata.head()


import pandas as pd
from sqlalchemy import create_engine
def import_DB(stock_name):
	db = pd.read_csv(stock_name+'.csv',index_col=False)
	engine=create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"  
						  .format(user="root", pw="password", 
						  db="stock"))
#engine=create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
# .format(user="root", pw="password",
#                      db="zipcode"))

	db.head()
	try:
		conn = msql.connect(host='localhost', user='root', password='password')
		if conn.is_connected():
			cursor = conn.cursor()
			cursor.execute('DROP DATABASE IF EXISTS '+stock_name+ ';')
			cursor.execute("CREATE DATABASE " + stock_name)
			print("created")
	except Error as e:
		print("Error ",e)

	try:
		conn = msql.connect(host='localhost', database=stock_name, user='root', password='password')
		if conn.is_connected():
			cursor = conn.cursor()
			cursor.execute('select database();')
			record= cursor.fetchone()
			print('connected')
	except Error as e:
		print("Error ",e)

	db.to_sql(stock_name, con = engine, if_exists = 'append', chunksize = 1000,index=False)


