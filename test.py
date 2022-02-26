import mysql.connector as msql
from mysql.connector import Error


import requests
import math
import argparse
import datetime as dt
import logging
import sys
import numpy as np
import meteomatics.api as api
import pandas as pd
import argparse
import logging
import numpy as np
import meteomatics.api as api
from meteomatics.logger import create_log_handler
from meteomatics._constants_ import LOGGERNAME



df = pd.read_csv ('code.csv' , sep =  ',')

header = df.columns.tolist()

a2d = df.to_numpy()

print("header : ",header)

CTC = dict()

for i in range(a2d.shape[0]):
	CTC[a2d[i][0]] = a2d[i][1]
	print(a2d[i][0],' ',CTC[a2d[i][0]])

CTC['Russia'] = 'ru'
CTC['US'] = 'us'
CTC['UK'] = 'UK'
r = requests.get('http://api.zippopotam.us/us/90210')
x = r.json()
place = x["places"][0]


print(place['longitude'])

df = pd.read_csv ('zip.csv' , sep =  ';')

header = df.columns.tolist()

print("header : ",header)

Dict = dict()

for i in range(len(header)):
	Dict[header[i]] = i

a2d = df.to_numpy()
print(a2d)
#newArr = np.ndarray(shape = (a2d.shape[0] , 1))
print(a2d.shape[0])
newArr = np.ndarray(shape = (a2d.shape[0] , 2))
for i in range(a2d.shape[0]):
	if a2d[i][10] == 'USA':
		a2d[i][10] = 'US'
	newArr[i][0] = 99999
	newArr[i][1] = 99999
	if (isinstance(a2d[i][9] , str) == True):
#	print(r.status_code, ' ',a2d[i][10], ' ',a2d[i][9])
		r = requests.get('http://api.zippopotam.us/'+CTC[a2d[i][10].strip()] + '/' + a2d[i][9])
		if (r.status_code == 200):
			x = r.json()
#			print(r.status_code, ' ',a2d[i][10], ' ',a2d[i][9])
			place = x["places"][0]
			newArr[i][0] = place["longitude"]
			newArr[i][1] = place["latitude"]
header.append("longitude")
header.append("latitude")

print(a2d.shape , newArr.shape)

add = np.append(a2d , newArr , axis=1)

print("add : ",add)
frame = pd.DataFrame(add , columns = header )
print("frame : ",frame)
frame.to_csv('updatedDB.csv')

from sqlalchemy import create_engine
db = pd.read_csv('updatedDB.csv',index_col=False)
engine=create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"  
                      .format(user="root", pw="password", 
                      db="classicmodels"))
db.head()
#try:
#	conn = msql.connect(host='localhost', user='root', password='password')
#	if conn.is_connected():
#		cursor = conn.cursor()
#		cursor.execute('DROP DATABASE IF EXISTS class;')
#		cursor.execute("CREATE DATABASE zipcode")
#		print("created")
#except Error as e:
#	print("Error ",e)

try:
	conn = msql.connect(auth_plugin='mysql_native_password', host='localhost', database='classicmodels', user='root', password='password')
	if conn.is_connected():
		cursor = conn.cursor()
		cursor.execute('select database();')
		record= cursor.fetchone()
		print('connected')
except Error as e:
	print("Error ",e)

db.to_sql('zipcode', con = engine, if_exists = 'append', chunksize = 1000,index=False)

