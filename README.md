# FINTECH DATA POOL

## Summary
A large volume of data is being generated on a continuous basis because of the massive growth of interconnected devices and the social websites. The increasing volume of data creates new challenges to data ingestion systems. One important task is to collect, ingest and integrate data from many sources into an analytics platform. The goal is having a meaningful and unique data pool that potentially possess high commercial value.

This project will get the daily data stock price from Yahoo Finance, a reliable API source, and Twitter tweets through Twitter API. From these two data sets, we want to see the connection between the tweets from the news as well as industry leaders and the stock prices in the two years.

## Copyright Disclaimer
<ins>This project contains these data:</ins>
-   Twitter, Tesla, and Bitcoin price acquired from Yahoo! Finance's API on April 28, 2022
-   Public tweets of 58 Twitter Accounts acquired from Twitter API on April 28, 2022
-   Public tweets of Elon Mustk from 2010 to March 2022 acquired from kaggle.com on April 28, 2022. The dataset is manually downloaded from the URL below
> https://www.kaggle.com/datasets/ayhmrba/elon-musk-tweets-2010-2021
-   List of 58 Twitter Usernames and their Twitter IDs manually acquired using tweeterid.com on April 15, 2022. These data is stored in ‘influencer.csv’ and ‘influencer.xlsx’ files.

## Development Environment Configuration
> python >= 3.7\
> pip install panda matplotlib mysql-connector yfinance

## Source Code Structure
```
./
│   README.md                       # Markdown file for source code document
│
└───Fintech_Backend                 # Source code to get data and display data visualization 
│   └───Finance                     # Source code to get Fintech data and display visualization
│   │   |   *.csv                   # Database in the CSV format
│   │   │   create_db.py            # Generate aggregation.csv contains stock and crypto prices
│   │   │   draw.py                 # Generate data visualization
│   │   │   to_DB.py                # Crawling Fintech data and store them in MySQL DB
│   │   │   twitter.csv             # All public tweets in one csv file. Complete database
│   │
│   └───Social_Network              # Source code to get Twitter data
│       └───data                    # Contains raw dataset
│       │   └───archive
│       │   │   └───Elon Musk
│       │   │       └───2017_2020   # Files from Kaggle for Elon Musk tweet from 2007 to 2020
│       │   │       │   │   *.csv   
│       │   │       │      
│       │   │       └───2021_2022   # Files from Kaggle for Elon Musk tweet from 2021 to 2022
│       │   │           │   *.csv   
│       │   │
│       │   │   archive.zip         # Compression file originally from Kaggle for Elon Mustk tweets
│       │   │   influencer.csv      # List of all Twitter ids of famous figures used for crawling
│       │   │   influencer.xlsx     # List of all Twitter ids of famous figures             
│       └───database
│       │   └─── csv
│       │        │   *.csv          # Crawled and cleaned database of all public tweets by user
│       └───lib                     # Contains modules to run the Twitter crawlers
│       │   │   api.py              # Define how the program get data from Twitter API 
│       │   │   connection.py       # Twitter API identification and MySQL connection info 
│       │   │   influencer.py       # Class to format Twitter users
│       │   │   tweet.py            # Class to format tweets
│       │   
│       │   cleaner.py              # Generate clean data of Elon Musk tweets from Kaggle dataset
│       │   injection.py            # Import all csv files (database/csv/*.csv) into MySQL DB
│       │   query.py                # Additional modules to merge and match with Fintech data
│       │   twitter.py              # Main program to crawl tweet data using Twitter API 
│       │   twitter.csv             # All public tweets in one csv file. Complete database
│       │   twitter.sql             # All public tweets, SQL script to export into MySQL DB
│               
└───Fintech_Frontend                # Empty - future works - server for data visualization 

```

## How to execute

### Get Twitter Data
<Updated on April 28, 2022>\
<ins>Notice:</ins> due to Twitter API inconsistency, Elon Musk public tweets cannot be acquired efficiently using Twitter API. It is recommended to download Elon Musk tweets manually on kaggle.com and place it into:
>./Fintech_Backend/Social_Network/data/archive/Elon Musk/2017_2020 | 2021_2022 

#### Crawl and Generate Database from Twitter
- Config Twitter API identification info in ./Fintech_Backend/Social_Network/lib/connection.py, then execute
>./Fintech_Backend/Social_Network> python cleaner.py\
>./Fintech_Backend/Social_Network> python twitter.py
#### Import Twitter Data into MySQL DB Server
- Config MySQL DB connection info in ./Fintech_Backend/Social_Network/lib/connection.py, then execute  
>./Fintech_Backend/Social_Network> python injection.py
>>All the tweets will be added into MySQL DB.\
>>A single twitter.csv file contains all public tweets will be generated after the execution

### Get Financial Data and Display Visualization
#### Visualization on crawled data 
> ./Fintech_Backend/Finance> python draw.py
#### To update Financial Data
-   Manually copy twitter.csv from ./Fintech_Backend/Social_Network to ./Fintech_Backend/Finance, then run
> ./Fintech_Backend/Finance> python create_db.py


