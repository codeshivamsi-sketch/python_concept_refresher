import os
from dotenv import load_dotenv

load_dotenv() 

db_url = os.getenv("DB_URL") # Wont work without calling load_dotenv()
print(db_url)




API_KEY = os.getenv("API_KEY", "abc123")
print(API_KEY)