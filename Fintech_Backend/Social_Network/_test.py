# import requests

# auth_headers = {
#     'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAABvXaQEAAAAARHMz0zV8nByUJv0sshlO1A4ZjTQ%3DEyvgEP67SyAseQTEZbf4TpSar4cA5Dr2sm1C5Zxw87LxugDZXz'    
# }

# raw_response = requests.get("https://api.twitter.com/2/users/44196397/tweets", headers=auth_headers)
# print(raw_response.json())

retry = 0
for retry in range(0, 5):
    pass

print(retry)