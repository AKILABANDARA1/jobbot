from fastapi import FastAPI

app = FastAPI()

from app import views  # Import routes to register with FastAPI
