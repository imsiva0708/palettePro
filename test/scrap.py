import requests
from bs4 import BeautifulSoup
def extract_main_image(recipe_url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(recipe_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        img_tags = soup.find_all('img')
        
        for img_tag in img_tags:
            if 'height' in img_tag.attrs and int(img_tag['height']) >= 300:
                image_url = img_tag.get('src')
                if image_url:
                    return image_url
        return None
    except requests.exceptions.RequestException as e:
        print("Error fetching URL:", e)
        return None


