from lib.api import Twitter_API_v2
from lib.influencer import Influencer
from lib.tweet import Tweet
from lib.connection import bearer_token, bearer_token_for_test, influencer_csv_path, CSV_Handle

from multiprocessing.pool import ThreadPool as Pool
from multiprocessing import Lock

pool_size = 1  # 5 concurrent api connections

def threaded_fetching_data(influencer_raw: Influencer, lock: Lock) -> None:
    twitter_api             = Twitter_API_v2(bearer_token)
    num_tweets              = 0
    
    cvs_user_handler        = CSV_Handle()
    tweet_dict_format_db    = []
    influencer              = Influencer(influencer_raw[0], influencer_raw[1], influencer_raw[2], influencer_raw[3])
    
    isCollected             = cvs_user_handler.isCollected(influencer.user_name)
    
    if isCollected:
        print(f"{influencer.user_name} is updating")
        num_tweets = 30 # check if there are up to new 24 tweets over the last 24 hours 
    else:
        print(f"{influencer.user_name} is freshly collecting")
        num_tweets = 3200 # get most 3200 recent tweets per user

    tweets_by_userid = twitter_api.get_tweets_by_user_id(
        influencer.twitter_user_id,
        _num_tweets = num_tweets, 
        _num_tweets_per_request = 10,
    )
    tweets_by_userid.reverse() # sort from oldest to newest

    lock.acquire()
    print("------******######------")
    print(influencer)
    print(len(tweets_by_userid))
    print("------******######------")
    lock.release()

    for tweet_raw_item in tweets_by_userid:
        tweet_record  = Tweet(influencer, tweet_raw_item)
        tweet_dict_format_db.append(tweet_record.toTuple())
    
    if isCollected: # update db csv
        tweet_record_list = cvs_user_handler.readCSVFile(influencer.user_name)
        tweet_record_list = tweet_record_list[-30:]
        tweet_dict_format_update_db = []

        # tweet_record: 
        # 0 <tweet_id> 
        # 1 <created_at> 
        # 2 <twitter_user_id> 
        # 3 <twitter_user_name> 
        # 4 <user_name> 
        # 5 <occupation> 
        # 6 <text>
        for tweet_old_record in tweet_record_list:
            for (idx, tweet_new_record) in enumerate(tweet_dict_format_db):    
                if str(tweet_old_record[4]) == str(tweet_new_record[4]):
                    del tweet_dict_format_db[idx]
        
        cvs_user_handler.writeListToCSVFile(f"{influencer.user_name}.csv", tweet_dict_format_db, isAppend=True)
    else: # writing a new file
        cvs_user_handler.writeListToCSVFile(f"{influencer.user_name}.csv", tweet_dict_format_db, isAppend=False)

def main():
    lock = Lock()
    # tweet_formatted_db = []

    # load list of influencers
    cvs_handler_read = CSV_Handle(influencer_csv_path)
    influencer_raw_list = cvs_handler_read.readCSVFile()

    pool_api_fetching = Pool(pool_size)

    # fetch data from api
    for influencer_raw in influencer_raw_list:
        pool_api_fetching.apply_async(threaded_fetching_data, (influencer_raw, lock))

    pool_api_fetching.close()
    pool_api_fetching.join()


if __name__ == "__main__":
    main()