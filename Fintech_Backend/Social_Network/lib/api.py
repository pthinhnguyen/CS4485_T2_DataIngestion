from urllib import response
import requests
import time

THRESHOLD = 5

def params__str__(params: dict) -> str:
    params_str = ""
    
    for key in params:
        if params[key] is not None:
            params_str = params_str + key + '=' + str(params[key]) + '&'

    # clean unnecessary '&'
    if params_str[-1] == '&': params_str = params_str[:-1]

    return params_str

class Twitter_API_v2:
    def __init__(self, bearer_token: str) -> None:
        self.bearer_token = bearer_token

    def get_tweets_by_user_id(self, _user_id: str, _start_time = None, _num_tweets=50, _num_tweets_per_request=50): #-> tuple[str]:
        response        = []
        number_requests = 0
        last_idx        = 0

        # calculate number of requests needed to retrive all required tweets
        if _num_tweets <= _num_tweets_per_request: 
            _num_tweets_per_request = _num_tweets
            number_requests = 1
            last_idx = 0
        else:
            number_requests = int(_num_tweets/_num_tweets_per_request)
            last_idx = number_requests - 1

        # set up parameter to send
        params = {
            'tweet.fields'          : 'created_at',
            'user.fields'           : None,
            'media.fields'          : None,
            'poll.fields'           : None,
            'place.fields'          : None,
            'max_results'           : _num_tweets_per_request,
            'pagination_token'      : None
        }

        # sending #(number_request) GET(s)
        for request_order in range(0, number_requests):
            params_str      = params__str__(params)
            retry           = 0
            result_count    = 0
            next_token      = ''
            meta            = None
            
            url = f"https://api.twitter.com/2/users/{_user_id}/tweets?{params_str}"
            auth_headers = {
                'Authorization': 'Bearer {}'.format(self.bearer_token)    
            }
            
            # each GET request retry up to THRESHOLD times
            for retry in range(0, THRESHOLD):
                # check if run out of quota
                raw_response = requests.get(url, headers=auth_headers).json()
                while ('status' in raw_response) and (int(raw_response['status']) == 429):
                    time.sleep(900) # wait for 15 min and try again
                    raw_response = requests.get(url, headers=auth_headers).json()

                # check if response contains data
                if 'meta' in raw_response:
                    meta_object = raw_response['meta']

                    if 'result_count' in meta_object:
                        try:   
                            result_count = int(meta_object['result_count'])
                        except:
                            result_count = 0
                        
                        if result_count < (80/100) * _num_tweets_per_request:
                            if request_order == last_idx:
                                if 'data' in raw_response:
                                    response.extend(list(raw_response['data']))
                                return response
                            else:
                                time.sleep(10)
                                pass
                        else:
                            if 'next_token' in meta_object:
                                next_token = str(meta_object['next_token'])
                                params['pagination_token'] = next_token

                                if 'data' in raw_response:
                                    response.extend(list(raw_response['data']))
                                break
                            else:
                                if request_order == last_idx:
                                    if 'data' in raw_response:
                                        response.extend(list(raw_response['data']))
                                    return response
                                else:
                                    next_token = ''
                                    time.sleep(10)
                                    pass    
                    else:
                        time.sleep(3)
                        result_count = 0
                        pass

                else: # no meta no data
                    time.sleep(3)
                    meta = None
                    pass
            
            if retry + 1 == THRESHOLD:
                if (result_count < (80/100) * _num_tweets_per_request) or (meta is None) or (not next_token):
                    if 'data' in raw_response:
                        response.extend(list(raw_response['data']))
                    break
                else:
                    pass

        return response


# url = f"https://api.twitter.com/2/users/{user_id}/tweets?tweet.fields=created_at&max_results=5&"       
# print(response.content)

