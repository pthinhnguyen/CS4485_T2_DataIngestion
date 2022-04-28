from re import T
import pandas as pd
import mysql.connector
from typing import Union
import datetime

csv_path = './twitter.csv'

Host = '192.168.15.138'
Port = 3306
UserName = 'admin'
PassWord = 'P@ssWorD'
DataBase = 'Twitter'

TWITTER_DATA = []

# tweet_record: 
# 0 <tweet_id> 
# 1 <created_at> 
# 2 <twitter_user_id> 
# 3 <twitter_user_name> 
# 4 <user_name> 
# 5 <occupation> 
# 6 <text>

# load from csv file
def loadFromCSV():
    data_frame = pd.read_csv(csv_path)
    return data_frame.values.tolist()

# load from SQL server
def loadFromSQL():
    cnn = mysql.connector.connect(
        host        = Host,
        port        = Port,
        user        = UserName,
        password    = PassWord,
        database    = DataBase,
        charset     = "utf8mb4", 
        use_unicode = True
    )
    
    crsr            = cnn.cursor()
    
    sql_select_Query = "select * from `tweets`"
    crsr.execute(sql_select_Query)
    records = crsr.fetchall()

    return records

TWITTER_DATA = loadFromCSV()
# TWITTER_DATA = loadFromSQL()

# print(len(TWITTER_DATA))

def filterDateTime(fromDate, toDate) -> list:
	filltered_datetime_tweets = []
	#try:
	#    fromDate = datetime.datetime(fromDate[0], fromDate[1], fromDate[2])
	#    toDate = datetime.datetime(toDate[0], toDate[1], toDate[2])
	#except:
	#    fromDate = datetime(2020, 12, 29)
	#    toDaye = datetime(2020, 12, 31)

	for tweet in TWITTER_DATA:
		try:
			if fromDate <= datetime.datetime.strptime(tweet[1], "%Y-%m-%d %H:%M:%S") <= toDate:
				filltered_datetime_tweets.append(tweet)
		except:
			pass
	return filltered_datetime_tweets

def filterDateTimeAuthor(fromDate , toDate , user):
	filtered_date_time = filterDateTime(fromDate , toDate)
	return_tweets = []
	for tweet in filtered_date_time:
		if tweet[3] == user:
			return_tweets.append(tweet)
	return return_tweets

import yfinance as yf
import pandas as pd
import numpy as np
def getDataSticker(ss ,  fromDate , toDate):
	data = yf.download(ss, start=fromDate, end=toDate)
	columns = np.asarray(data.columns)
	fields = np.asarray(data.to_numpy() , dtype = 'float32')
#print(columns)
#print(data.to_numpy())

	frame = pd.DataFrame(fields , columns = columns )
#print("frame : ",frame)
	frame.to_csv(ss+'.csv')
	return fields
#print(getDataSticker("BTC-USD" , "2022-01-01" , "2022-05-01"))
print(len(filterDateTimeAuthor(datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 7) , "@elonmusk")))
