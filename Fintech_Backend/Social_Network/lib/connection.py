bearer_token_for_test = 'AAAAAAAAAAAAAAAAAAAAABvXaQEAAAAARHMz0zV8nByUJv0sshlO1A4ZjTQ%3DEyvgEP67SyAseQTEZbf4TpSar4cA5Dr2sm1C5Zxw87LxugDZXz'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAG%2BIbAEAAAAA%2BnB2n5h%2BXnZc%2BHRmzQ6vaaD3pxw%3D8UOUwiU0YjT7AwLR9uh5lluWOKt2aFgkgJTFLly0jGlOqRdKJz'
influencer_csv_path = './data/influencer.csv'
db_csv_path = './database/csv'

Host = '192.168.15.138'
Port = 3306
UserName = 'admin'
PassWord = 'P@ssWorD'

import pandas as pd
import csv
from os.path import exists
import mysql.connector

class CSV_Handle:
    def __init__(self, influencer_csv_path = None) -> None:
        self.influencer_csv_path = influencer_csv_path
        pass
    
    def readCSVFile(self, user_name = ''):
        try:
            if self.influencer_csv_path is not None:
                data_frame = pd.read_csv(self.influencer_csv_path)
                return data_frame.values.tolist()
            else:
                path = f"{db_csv_path}/{user_name}.csv"
                data_frame = pd.read_csv(path)                   
                return data_frame.values.tolist()
        except:
            return []
    
    def writeListToCSVFile(self, file_name: str, object_list: list, isAppend = False) -> None:
        path = f"{db_csv_path}/{file_name}"
        if isAppend:
            with open(path, 'a', encoding='UTF8', newline='') as file_handler:
                writer = csv.writer(file_handler)
                writer.writerows(object_list)
        else:
            with open(path, 'w', encoding='UTF8', newline='') as file_handler:
                writer = csv.writer(file_handler)
                writer.writerows(object_list)            
    
    def isExist(self, path_to_file: str) -> bool:
        isExist = exists(path_to_file)
        return bool(isExist)

    def isCollected(self, user_name: str):
        path        = f"{db_csv_path}/{user_name}.csv"
        isCollected = self.isExist(path)

        return isCollected

class MySQL_Handle:
    def __init__(self, host, port, user, password, database = None) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def mysqlConnector(self):
        mydb = None
        
        if self.database is None:
            mydb = mysql.connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password
            )
        else:
            mydb = mysql.connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database,
                charset ="utf8mb4", 
                use_unicode=True
            )

        return mydb


