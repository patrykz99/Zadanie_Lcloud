from dotenv import load_dotenv
from pathlib import Path
import os 

dir_path = Path(__file__).resolve().parent
env_variables = dir_path / '.env'

load_dotenv(env_variables)

class Config:
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    
    
print(Config().AWS_ACCESS_KEY_ID)
