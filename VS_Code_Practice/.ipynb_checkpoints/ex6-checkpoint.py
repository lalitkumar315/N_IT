from dotenv import load_dotenv
print(load_dotenv())
import os
name = os.getenv('NAME')
age = os.getenv('AGE')
print(f'Name is {name}')
print(f'Age is {age}')