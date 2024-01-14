import requests
#?order=desc&sort=activity&site=stackoverflow
api_address =  "https://api.stackexchange.com/"
question = "/2.3/questions?order=desc&sort=activity&site=stackoverflow"
response = requests.get(api_address+question)
print(api_address+question)
print(response.json())