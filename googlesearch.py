import requests
import os
# import json 
from scrap import extract_main_image

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
    link = results['items'][0]['link']
    title = results['items'][0]['title']
    list=[]
    list.append(link)
    list.append(title)
    list.append(extract_main_image(link))
    return list

