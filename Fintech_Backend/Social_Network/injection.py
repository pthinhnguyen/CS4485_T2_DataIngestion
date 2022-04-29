 # -*- coding: utf-8 -*-

from lib.connection import Host, Port, UserName, PassWord, MySQL_Handle, CSV_Handle, db_csv_path, mysql

import pandas as pd
import os
import glob
import datetime

import csv

from lib.tweet import Tweet

mysql_handler   = MySQL_Handle(Host, Port, UserName, PassWord)
mydb            = mysql_handler.mysqlConnector()
mycursor        = mydb.cursor()

mycursor.execute('CREATE DATABASE IF NOT EXISTS Twitter CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;')

mysql_handler   = MySQL_Handle(Host, Port, UserName, PassWord, database = 'Twitter')
mydb            = mysql_handler.mysqlConnector()
mycursor        = mydb.cursor()


# mycursor.execute("""CREATE TABLE IF NOT EXISTS `tweets` (
#             `tweet_id` BIGINT NOT NULL,
#             `created_at` TIMESTAMP,
#             `twitter_user_id` BIGINT,
#             `twitter_user_name` VARCHAR(255),
#             `user_name` VARCHAR(255),
#             `occupation`VARCHAR(255),
#             `text`LONGTEXT,
#             CONSTRAINT PK_tweet PRIMARY KEY (tweet_id)
#         );"""
#     )

# csv_db_files = glob.glob(os.path.join(db_csv_path, "*.csv"))
# tweets = []
# for file_path in csv_db_files:
#     csv_handler = CSV_Handle(file_path)
#     tweets.extend(csv_handler.readCSVFile())

# # print(len(tweets))
# # exit()

# name = ''
# for tweet in tweets:
#     try:
#         tweet_id            = int(tweet[0])
#         created_at          = datetime.datetime.strptime(tweet[1][:19].replace("T"," "), '%Y-%m-%d %H:%M:%S')
#         twitter_user_id     = int(tweet[2])
#         twitter_user_name   = tweet[3]
#         user_name           = tweet[4]
#         occupation          = tweet[5]
#         text                = tweet[6]

#         if name != user_name:
#             name = user_name
#             print(name)

#         sql = """INSERT INTO `tweets`
#                 (tweet_id, created_at, twitter_user_id, twitter_user_name, user_name, occupation, text)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
#         val = (tweet_id, created_at, twitter_user_id, twitter_user_name, user_name, occupation, text)
#         mycursor.execute(sql, val)
#     except (mysql.connector.Error, ValueError) as err:
#         print("MySQL Query Error: {}".format(err))
#         # mydb.rollback()

# mydb.commit()


sql_select_Query = "select * from `tweets`"
mycursor.execute(sql_select_Query)
records = mycursor.fetchall()
print(len(records))

with open("./twitter.csv", 'w', encoding='UTF8', newline='') as file_handler:
    writer = csv.writer(file_handler)
    writer.writerow(["tweet_id", "created_at", "twitter_user_id", "twitter_user_name", "user_name", "occupation", "text"])
    writer.writerows(records)   

mydb.close()