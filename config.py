from dotenv import load_dotenv
from pathlib import Path
import os

base_dir = Path(__file__).resolve().parent  #ściażka do folderu zawierajcego plik cofig.py
env_file = base_dir / ".env"    #ścieżka do pliku .env
load_dotenv(env_file)   # ładowanie z pliku zmiennych środowiskowych
DB_FILE_PATH = base_dir / "db" / 'tasks.db'


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE_PATH}'

config = Config()