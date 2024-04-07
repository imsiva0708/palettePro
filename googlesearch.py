import requests
import os
import json 

API_KEY = os.getenv('GOOGLE_CUSTOM_SEARCH_API_KEY')
SEARCH_ID = os.getenv('GOOGLE_SEARCH_ENGINE_ID')

url = 'https://www.googleapis.com/customsearch/v1'
def search(item):
    search_query = f'recipe for {item}'
    params = {
        'q' : search_query,
        'key' : API_KEY,
        'cx': SEARCH_ID
    }

    response = requests.get(url,params=params)
    results = response.json()
    print(results['items'][0]['link'])
