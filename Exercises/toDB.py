import argparse
import datetime as dt
import logging
import sys
import numpy as np
import meteomatics.api as api
from meteomatics.logger import create_log_handler
from meteomatics._constants_ import LOGGERNAME
import pandas as pd


username = "na_vu"
password = "Gx9mHptR5TA6k"
coordinate = [(30.51,-97.50)]
model = 'mix'
#startdate = dt.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0) - dt.timedelta(days=1)
startdate = dt.datetime.utcnow() #- dt.timedelta(days=1)
enddate = startdate #+ dt.timedelta(days=1)
interval = dt.timedelta(hours=1)
parameters = ['t_2m:C']
data = api.query_time_series(coordinate, startdate,enddate,interval,parameters, username, password, model=model)
header = data.columns.tolist()
print("header : ",header)

data = data.to_numpy()
print (data)
df = pd.read_csv (r'zipcode.csv')
header = df.columns.tolist()
print("header : ",header)
Dict = dict()

for i in range(len(header)):
	Dict[header[i]] = i

a2d = df.to_numpy()
print(a2d)
newArr = np.ndarray(shape = (a2d.shape[0] , 1))
print(a2d.shape[0])
for i in range(10):
	indx1 = Dict['Lat']
	indx2 = Dict['Long']
	coordinate = [(a2d[i][indx1] , a2d[i][indx2])]
	data = api.query_time_series(coordinate, startdate,enddate,interval,parameters, username, password, model=model)
	newArr[i][0] = data.to_numpy()[0][0]
#print("getting data ",i)
print(a2d.shape , newArr.shape)
add = np.append(a2d , newArr , axis=1)

print("add : ",add)

header.append("temp")
frame = pd.DataFrame(add , columns = header )
print("frame : ",frame)
frame.to_csv('updatedDB.csv')




from sqlalchemy import create_engine
db = pd.read_csv('updatedDB.csv',index_col=False)
engine=create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                      .format(user="root", pw="password",
                      db="zipcode"))
db.head()
try:
	conn = msql.connect(host='localhost', user='root', password='password')
	if conn.is_connected():
		cursor = conn.cursor()
		cursor.execute('DROP DATABASE IF EXISTS updatedCustomer;')
		cursor.execute("CREATE DATABASE updatedCustomer")
		print("created")
except Error as e:
	print("Error ",e)

try:
	conn = msql.connect(host='localhost', database='updatedCustomer', user='root', password='password')
	if conn.is_connected():
		cursor = conn.cursor()
		cursor.execute('select database();')
		record= cursor.fetchone()
		print('connected')
except Error as e:
	print("Error ",e)

db.to_sql('updatedCustomer', con = engine, if_exists = 'append', chunksize = 1000,index=False)

