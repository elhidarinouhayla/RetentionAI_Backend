from app.database import Base
from pydantic import BaseModel
from sqlalchemy import String, Integer, Column



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False )
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)