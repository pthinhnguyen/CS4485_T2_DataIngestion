
class Influencer:
    def __init__(self, user_ame: str, tweeter_user_name: str, tweeter_user_id: str ) -> None:
        self.user_name = user_ame
        self.twitter_user_name = tweeter_user_name
        self.twitter_user_id = int(tweeter_user_id)

    def __repr__(self) -> str:
        return "('%s', '%s', %d)" % (self.name, self.tweeter_username, self.tweeter_id) 
    
    def __str__(self) -> str:
        return "('%s', '%s', %d)" % (self.name, self.tweeter_username, self.tweeter_id)
    