import google.generativeai as genai
from dotenv import load_dotenv
import os
print(load_dotenv())
genai.configure(api_key =os.getenv('API_KEY'))
model=genai.GenerativeModel('gemini-2.5-flash')
print(model.generate_content('Who are top 5 cricketer i india?'))