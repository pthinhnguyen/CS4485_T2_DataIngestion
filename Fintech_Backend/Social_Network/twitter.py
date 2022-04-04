from twitter_token import bearer_token_for_test
from api import Twitter_API_v2
from influencer import Influencer
from tweet import Tweet

import pandas as pd
import json

def main():
    twitter_api = Twitter_API_v2(bearer_token_for_test)
    tweet_formatted_db = []

    # load list of influencers
    data_frame = pd.read_csv('./data/influencer.csv')
    influencer_raw_list = data_frame.values.tolist()

    for influencer_raw in influencer_raw_list:
        influencer          = Influencer(influencer_raw[0], influencer_raw[1], str(influencer_raw[2]))
        tweets_by_userid    = twitter_api.get_tweets_by_user_id(influencer.twitter_user_id, _num_tweets=5)
        
        for tweet_item in tweets_by_userid:
            tweet_formatted_db.append(Tweet(influencer, tweet_item))

    print(tweet_formatted_db)


if __name__ == "__main__":
    main()