from influencer import Influencer


class Tweet:
    def __init__(self, user: Influencer, tweet_item: dict) -> None:
        self.user_name = user.user_name
        self.twitter_user_name = user.twitter_user_name
        self.twitter_user_id = user.twitter_user_id
        self.tweet_id = tweet_item['id']
        self.text = tweet_item['text']
        self.created_at = tweet_item['created_at']

    def __repr__(self) -> str:
        return f"{self.user_name},{self.twitter_user_name},{self.twitter_user_id},{self.tweet_id},{self.text},{self.created_at}"
    
    def __str__(self) -> str:
        return f"{self.user_name},{self.twitter_user_name},{self.twitter_user_id},{self.tweet_id},{self.text},{self.created_at}"        