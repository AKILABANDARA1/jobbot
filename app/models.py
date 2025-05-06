from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import Config

Base = declarative_base()

class UserPreference(Base):
    __tablename__ = 'preferences'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    keywords = Column(String)

engine = create_engine(Config.DB_URL)
SessionLocal = sessionmaker(bind=engine)

