import requests
import json
import user_input

API_KEY = "tBfVpT4RMkNj"
PROJECT_TOKEN = 'ta4TO7wT8gFJ'
RUN_TOKEN = 'te_3iOeVXcNg'

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={'api_key': API_KEY})
data = json.loads(response.text)

with open('dict.json') as file: 
    dict = json.load(file) 

output = data['french_urls'][int(dict[user_input.vrb()])][user_input.tns()]
