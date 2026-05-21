import os
from dotenv import load_dotenv
load_dotenv()
pas = os.getenv("password")
print(pas)