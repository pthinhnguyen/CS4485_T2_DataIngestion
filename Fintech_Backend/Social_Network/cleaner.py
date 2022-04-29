elon_musk_raw_csv_data_2017_2020 = "./data/archive/Elon Musk/2017_2020"
elon_musk_raw_csv_data_2021_2022 = "./data/archive/Elon Musk/2021_2022"

from lib.connection import CSV_Handle

import pandas as pd
import os
import glob
import re
import datetime
import pytz

local = pytz.timezone("Asia/Aden")
date_format = "%Y-%m-%dT%H:%M:%S.%fZ" 

# path = os.getcwd(elon_musk_raw_csv_data)
csv_files_2017_2020 = glob.glob(os.path.join(elon_musk_raw_csv_data_2017_2020, "*.csv"))
csv_files_2021_2022 = glob.glob(os.path.join(elon_musk_raw_csv_data_2021_2022, "*.csv"))

raw_tweets                  = []
raw_clean_tweets            = []
raw_tweets_2021_2022        = []
raw_clean_tweets_2021_2022  = []

for file_path in csv_files_2017_2020:
    csv_handler = CSV_Handle(file_path)
    raw_tweets.extend(csv_handler.readCSVFile())

for file_path in csv_files_2021_2022:
    csv_handler = CSV_Handle(file_path)
    raw_tweets_2021_2022.extend(csv_handler.readCSVFile())

for raw_tweet in raw_tweets:
    raw_clean_tweet = []
    raw_clean_tweet.append(raw_tweet[1])
    
    
    utc_dt = str(raw_tweet[4]).replace(" ", 'T') + ".000Z"    
    raw_clean_tweet.append(utc_dt)
    
    raw_clean_tweet.append(raw_tweet[11])
    raw_clean_tweet.append('@' + raw_tweet[13])
    raw_clean_tweet.append(raw_tweet[14])
    raw_clean_tweet.append("Business Man")
    raw_clean_tweet.append(raw_tweet[7])

    raw_clean_tweets.append(raw_clean_tweet)

for raw_tweet_2021_2022 in raw_tweets_2021_2022:
    raw_clean_tweet_2021_2022 = []
    raw_clean_tweet_2021_2022.append(raw_tweet_2021_2022[0])
    
    local_time_string = (re.sub("[A-Za-z]", "", raw_tweet_2021_2022[2])).rstrip()
    local_datetime_object = datetime.datetime.strptime(local_time_string, '%Y-%m-%d %H:%M:%S')
    local_dt = local.localize(local_datetime_object, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    utc_dt = (str(utc_dt)[0:19]).replace(" ", 'T') + ".000Z"    
    raw_clean_tweet_2021_2022.append(utc_dt)

    raw_clean_tweet_2021_2022.append(raw_tweet_2021_2022[6])
    raw_clean_tweet_2021_2022.append('@' + raw_tweet_2021_2022[7])
    raw_clean_tweet_2021_2022.append(raw_tweet_2021_2022[8])
    raw_clean_tweet_2021_2022.append("Business Man")
    raw_clean_tweet_2021_2022.append(raw_tweet_2021_2022[10])

    raw_clean_tweets_2021_2022.append(raw_clean_tweet_2021_2022)

# print(raw_clean_tweets[0])
# print(raw_clean_tweets_2021_2022[100])   

clean_data = []
clean_data.extend(raw_clean_tweets)
clean_data.extend(raw_clean_tweets_2021_2022)

print(clean_data[3000])
print(clean_data[27000])

cvs_user_writer = CSV_Handle()
cvs_user_writer.writeListToCSVFile("Elon Musk.csv", clean_data, isAppend=False)
 

