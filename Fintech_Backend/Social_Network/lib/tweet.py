
class Tweet:
    def __init__(self, user: object, tweet_item: dict) -> None:
        if user is not None:
            try:
                self.user_name          = user.user_name
                self.twitter_user_name  = user.twitter_user_name
                self.occupation         = user.occupation
                self.twitter_user_id    = user.twitter_user_id
            except:
                self.user_name          = ''
                self.twitter_user_name  = ''
                self.occupation         = ''
                self.twitter_user_id    = ''
        else:
            self.user_name              = ''
            self.twitter_user_name      = ''
            self.occupation             = ''
            self.twitter_user_id        = ''
        
        if tweet_item is not None:
            try:
                self.tweet_id           = tweet_item['id']
                self.text               = tweet_item['text']
                self.created_at         = tweet_item['created_at']
            except:
                self.tweet_id           = ''
                self.text               = ''
                self.created_at         = ''
        else:
            self.tweet_id               = ''
            self.text                   = ''
            self.created_at             = ''

    def __repr__(self) -> str:
        return f"{self.tweet_id},{self.created_at},{self.twitter_user_id},{self.twitter_user_name},{self.user_name},{self.occupation},{self.text}"

    def __str__(self) -> str:
        return f"{self.tweet_id},{self.created_at},{self.twitter_user_id},{self.twitter_user_name},{self.user_name},{self.occupation},{self.text}"
    
    def toTuple(self):
        return (
            self.tweet_id,
            self.created_at,
            self.twitter_user_id,
            self.twitter_user_name,
            self.user_name,
            self.occupation,
            self.text,
        )

    def __eq__(self, user: object) -> bool:
        if self.tweet_id == user.tweet_id: return True
        return False