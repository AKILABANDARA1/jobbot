import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_URL = os.getenv("DATABASE_URL", "sqlite:///./jobs.db")
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
