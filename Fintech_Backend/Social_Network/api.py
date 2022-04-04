from urllib import response
import requests

def params__str__(params: dict) -> str:
    params_str = ""
    
    for key in params:
        if params[key] is not None:
            params_str = params_str + key + '=' + str(params[key]) + '&'

    return params_str

class Twitter_API_v2:
    def __init__(self, bearer_token: str) -> None:
        self.bearer_token = bearer_token

    def get_tweets_by_user_id(self, _user_id: str, _start_time = None, _num_tweets = 100) -> tuple[str]:
        user_id = _user_id
        params = {
            'tweet.fields'  : 'created_at',
            'user.fields'   : None,
            'media.fields'  : None,
            'poll.fields'   : None,
            'place.fields'  : None,
            'max_results'   : _num_tweets
        }
        params_str = params__str__(params)
        
        url = f"https://api.twitter.com/2/users/{user_id}/tweets?{params_str}"  
        auth_headers = {
            'Authorization': 'Bearer {}'.format(self.bearer_token)    
        }
        
        response = tuple(requests.get(url, headers=auth_headers).json()["data"])
        return response


# url = f"https://api.twitter.com/2/users/{user_id}/tweets?tweet.fields=created_at&max_results=5&"       
# print(response.content)

