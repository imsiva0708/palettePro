import os
import googlesearch
import google.generativeai as genai

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

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])
items = [x for x in input("Enter ingredients: ").split(' ')]
convo.send_message(f"Act as an experienced chef and homecook. generate me list of food items where the key ingredients are all of {items};output the items in a single line seperated by commas")
# print(convo.last.text)
list = convo.last.text.split(',')
print(list)
for item in list:
    googlesearch.search(item)