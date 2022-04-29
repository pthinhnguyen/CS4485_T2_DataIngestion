
class Influencer:
    def __init__(self, user_name: str, tweeter_user_name: str, occupation: str, tweeter_user_id: str ) -> None:
        self.user_name          = user_name
        self.twitter_user_name  = tweeter_user_name
        self.occupation         = occupation
        self.twitter_user_id    = str(tweeter_user_id)

    def __repr__(self) -> str:
        return "('%s', '%s', '%s', %s)" % (self.user_name, self.twitter_user_name, self.occupation, self.twitter_user_id) 
    
    def __str__(self) -> str:
        return "('%s', '%s', '%s', %s)" % (self.user_name, self.twitter_user_name, self.occupation, self.twitter_user_id)

    