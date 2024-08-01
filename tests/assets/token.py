from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def get_access_token():
    load_dotenv(dotenv_path=os.path.join(BASE_DIR,".env"))
    access_token = os.getenv("ACCESS_TOKEN")
    if not access_token:
        raise ValueError("ACCESS_TOKEN not found in environment variables")
    return access_token

