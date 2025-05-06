from fastapi import APIRouter, Request
from app.models import SessionLocal, UserPreference

router = APIRouter()

@router.get("/")
async def welcome():
    return {"message": "Welcome to the Job Alert Bot"}

@router.post("/subscribe/")
async def subscribe(email: str, keywords: str):
    db = SessionLocal()
    pref = UserPreference(email=email, keywords=keywords)
    db.add(pref)
    db.commit()
    return {"status": "subscribed"}

