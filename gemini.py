import os
import googlesearch
import google.generativeai as genai
from stringmaker import stringmaker
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()
genai.configure(api_key=f"{os.getenv('GEMINI_API_KEY')}")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
def getRecipe(items):
    convo = model.start_chat(history=[])
    convo.send_message(f"Act as an experienced chef and homecook. generate me a list of food items where the main ingredients are all of {items}; output the list in a single line seperated by $ symbol")
    print(convo.last.text)
    recipe_list = convo.last.text.split('$')
    print(f'In recipe list : {recipe_list}')
    return recipe_list
# getRecipe(['onion','tomato','potato'])